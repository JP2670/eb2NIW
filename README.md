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
- Around **$30–$40** to process ~7,700 PDFs using GPT-4o-mini model (April 2025 prices).

---

# ✍️ How to Customize for Your Own Petition

Before running the script, you need to **tell the program what your own EB2-NIW petition looks like**.

You do this by **editing** the following part of `process_eb2niw_prongs_compare.py`:

---

## 📋 Where to Edit in the Script

In the beginning of the script, you will find this block:

```python
my_case = {
    "Prong1": "Summarize why your National Importance is strong",
    "Prong2": "Summarize why you are Well Positioned",
    "Prong3": "Summarize why Labor Waiver is justified for you"
}
```

You need to **replace the example texts** with **short 1–2 sentence summaries** based on your real EB2-NIW petition.

---

## 🧠 Example 1: Generic STEM Professional 

```python
my_case = {
    "Prong1": "Strong: working on cutting-edge technology aligned with U.S. innovation goals.",
    "Prong2": "5+ years professional experience in major U.S. organizations, demonstrated leadership roles.",
    "Prong3": "Immediate contribution to national innovation efforts; delay would harm competitiveness."
}
```

---

## 🧪 Example 2: AI Researcher (Machine Learning for Healthcare)

```python
my_case = {
    "Prong1": "Strong: Research directly improves U.S. healthcare outcomes using AI for early disease detection.",
    "Prong2": "4+ years leading projects at a top U.S. university hospital and multiple published papers.",
    "Prong3": "Immediate healthcare application; delay would risk public health improvements."
}
```

---

## 💼 Example 3: Finance Professional (Economic Policy Advisor)

```python
my_case = {
    "Prong1": "Strong: Directly advising U.S. state governments on economic policy initiatives.",
    "Prong2": "8 years of leadership roles in U.S. think tanks, direct policy impact proven.",
    "Prong3": "Delay would harm ongoing critical public sector projects; immediate national impact needed."
}
```

# ⚡ Tips for Writing Your Own Prongs:

- Be short (1–2 sentences max)
- Be direct: mention **U.S. impact**, **leadership**, **urgency**
- Match the style you would use in your NIW petition or recommendation letters
- No need to write full essays — this is just for automated comparison.

---

✅ This will make your script work correctly for *your unique situation*!

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
