# === process_eb2niw_prongs_compare.py ===

import openai
import requests
import fitz  # PyMuPDF
import csv
import time

# ---------------
# SETTINGS
# ---------------
openai.api_key = "YOUR_NEW_OPENAI_API_KEY_HERE"
model_name = "gpt-4o"
batch_size = 50
sleep_time = 10
start_line = 1  # <-- Change here: starting line number (1-indexed)
end_line = 7700  # <-- Change here: ending line number (inclusive), I would first run a trial with 10 cases.
#7700 cases will take some time, start with a smaller number initially.

# Your petition details hardcoded
my_case = {
    "Prong1": "Strong: working on cutting-edge technology aligned with U.S. innovation goals.",
    "Prong2": "5+ years professional experience in major U.S. organizations, demonstrated leadership roles.",
    "Prong3": "Immediate contribution to national innovation efforts; delay would harm competitiveness."
}


# ---------------
# READ PDF LINKS
# ---------------
with open("Master_file", "r") as file:
    all_links = [line.strip() for line in file if line.strip()]

pdf_links = all_links[start_line - 1:end_line]

# ---------------
# HELPER FUNCTIONS
# ---------------

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=20)
        if response.status_code != 200:
            print(f"Failed to fetch {url}")
            return ""
        with open("temp.pdf", "wb") as f:
            f.write(response.content)
        doc = fitz.open("temp.pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error fetching PDF from {url}: {e}")
        return ""

def analyze_niw_case(text):
    prompt = f"""
You are an immigration expert.
The following text is a USCIS decision document.

First:
- Determine if this case is an EB-2 NIw petition. Answer Yes or No.

If Yes, then:
- Summarize issues for each NIW prong if rejection happened:
  1. Prong 1 (Substantial Merit and National Importance)
  2. Prong 2 (Well Positioned to Advance Endeavor)
  3. Prong 3 (Benefit to U.S. and PERM Waiver justified)
- Write short 1-2 sentences for each prong explaining the failure reason.

If No, just say: "Not an NIW case."

Document Text:
{text[:12000]}
"""
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1200,
        )
        summary = response['choices'][0]['message']['content']
        return summary
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Error"

def compare_prongs(prong_reason, my_case_reason):
    prong_reason_lower = prong_reason.lower()
    if any(x in prong_reason_lower for x in ["weak", "missing", "lack", "no"]):
        return "Your case stronger"
    elif "strong" in prong_reason_lower or "good" in prong_reason_lower:
        return "Mixed"
    else:
        return "Mixed"

# ---------------
# PROCESS PDFs
# ---------------

output_rows = []

for idx, link in enumerate(pdf_links):
    print(f"Processing {start_line + idx}/{end_line}: {link}")
    text = extract_text_from_url(link)
    if not text:
        continue

    summary = analyze_niw_case(text)

    if "Not an NIW case" in summary:
        output_rows.append([link, "Not NIW", "Not NIW", "Not NIW", "-", "-", "-", "Not NIW"])
    else:
        try:
            prong1 = prong2 = prong3 = ""
            lines = summary.split('\n')
            for line in lines:
                if "Prong 1" in line:
                    prong1 = line.split(":",1)[-1].strip()
                if "Prong 2" in line:
                    prong2 = line.split(":",1)[-1].strip()
                if "Prong 3" in line:
                    prong3 = line.split(":",1)[-1].strip()

            prong1_verdict = compare_prongs(prong1, my_case['Prong1'])
            prong2_verdict = compare_prongs(prong2, my_case['Prong2'])
            prong3_verdict = compare_prongs(prong3, my_case['Prong3'])

            # Determine overall verdict
            if prong1_verdict == prong2_verdict == prong3_verdict == "Your case stronger":
                final_verdict = "Your case much stronger"
            elif "Your case stronger" in [prong1_verdict, prong2_verdict, prong3_verdict]:
                final_verdict = "Your case slightly stronger"
            else:
                final_verdict = "Mixed or equal"

            output_rows.append([link, prong1, prong2, prong3, prong1_verdict, prong2_verdict, prong3_verdict, final_verdict])

        except Exception as e:
            print(f"Error parsing prongs: {e}")
            output_rows.append([link, "Parse Error", "Parse Error", "Parse Error", "-", "-", "-", "Parse Error"])

    if (idx + 1) % batch_size == 0 or (idx + 1) == len(pdf_links):
        print("Saving progress...")
        with open("summary_prongs_comparison.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["PDF Link", "Prong 1 Reason", "Prong 2 Reason", "Prong 3 Reason", "Prong 1 Verdict", "Prong 2 Verdict", "Prong 3 Verdict", "Final Verdict"])
            writer.writerows(output_rows)
        print(f"Saved {len(output_rows)} rows so far.")
        time.sleep(sleep_time)

print("Done! All selected NIW prong comparisons saved to summary_prongs_comparison.csv")
