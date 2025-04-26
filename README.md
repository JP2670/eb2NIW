# EB2-NIW Petition Case Comparator 🚀

This Python script reads USCIS AAO decision PDFs, extracts the main reasons for denial (for the 3 NIW prongs), and **compares** each case **side-by-side** with your own EB2-NIW petition strengths.

You can automatically **compare your case against 7,800+ real AAO decisions**!

---

## 📦 Features

- Scrape USCIS AAO PDF decision documents
- Use OpenAI GPT-4o model to summarize NIW prong failure reasons
- Compare each decision to your own petition
- Batch processing for thousands of PDFs
- Clean CSV file output for easy review

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/niw_case_comparator.git
cd niw_case_comparator
pip install -r requirements.txt
```

---

## 🔑 Setting Up OpenAI API Access

This script uses OpenAI GPT-4o model.  
You need an OpenAI API key to use it.

- Signup for free at: [https://platform.openai.com/signup](https://platform.openai.com/signup)
- After signup, go to [API Keys page](https://platform.openai.com/account/api-keys)
- Click **Create New Secret Key** and copy it
- Paste your API key inside the Python script here:

```python
openai.api_key = "your-api-key-here"
```

**⚡ Important:** You will need to add a small amount of balance ($5–$10) to your OpenAI account to run this full project.

Cost estimate:
- Around **$20–$23** to process ~7,800 PDFs using GPT-4o-mini model (April 2025 prices).

---

## ✍️ How to Customize For Your Own Petition

You must hardcode your own petition's strengths inside the script.  
In `process_eb2niw_prongs_compare.py`, update the following dictionary:

```python
my_case = {
    "Prong1": "Summarize why your National Importance is strong",
    "Prong2": "Summarize why you are Well Positioned",
    "Prong3": "Summarize why Labor Waiver is justified for you"
}
```

👉 Use simple, 1-2 sentence summary for each prong based on your own EB2-NIW petition.

---

## 📄 Output

The script will generate a file called `summary_prongs_comparison.csv` with the following columns:

| Column | Description |
|:---|:---|
| PDF Link | Link to original AAO decision |
| Prong 1 Reason | Why Prong 1 failed for that case |
| Prong 2 Reason | Why Prong 2 failed |
| Prong 3 Reason | Why Prong 3 failed |
| Prong 1 Verdict | Your case stronger / Mixed |
| Prong 2 Verdict | Your case stronger / Mixed |
| Prong 3 Verdict | Your case stronger / Mixed |
| Final Verdict | Overall assessment: Stronger / Mixed |

---

## 🛠 Notes

- The Master_file provided contains over 7,800 AAO decision PDF links (as of April 2025).
- Some non-EB2-NIW cases are mixed in (e.g., EB-1, EB-3) — filtering is a future update.
- The script automatically detects non-NIW cases and marks them.
- For 'mixed' verdict cases, you can manually check the PDF links to make your own detailed judgment.
- You can even use the PDF link with ChatGPT to create deeper comparisons with your petition if needed.

---

## ❤️ Contribute

Pull requests, improvements, and feature ideas are welcome!

---

# 📜 License

Open-source for personal and educational use.

---
