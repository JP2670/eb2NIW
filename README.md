# EB2-NIW Petition Case Comparator 🚀

This Python script reads USCIS AAO decision PDFs, extracts the main reasons for denial (3 NIW prongs), and **compares** them **side-by-side** with your own EB2-NIW petition strengths.

You can analyze thousands of cases and see **how your petition compares**!

---

## Features

- Scrape USCIS PDF decision documents
- Use OpenAI GPT-4o or 4o-mini model to summarize NIW prong issues
- Compare each prong (Prong 1, Prong 2, Prong 3) to your own petition
- Batch mode (process 50 cases at a time)
- Output clean CSV file for easy review

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/niw_case_comparator.git
cd niw_case_comparator
pip install -r requirements.txt
```

---

## How to Use

1. Prepare a `Master_file` — a simple text file with 1 PDF link per line.
2. Set your `OpenAI API key` inside the script.
3. Set `start_line` and `end_line` inside the script to pick which links to process.
4. Run the script:

```bash
python process_eb2niw_prongs_compare.py
```

After processing, you will get `summary_prongs_comparison.csv` file.

---

## Notes

- You need OpenAI API key (GPT-4o model)
- Costs approximately ~$23 to process ~7,800 PDFs (very affordable)
- Script automatically handles batch saving and slow server response
- Works perfectly on Mac, Linux, and Windows

---

## License

Open-source for educational and personal use.  
Please respect USCIS terms and public data usage.

---

# ❤️ Contribution

If you improve the script (like adding resume feature or auto-pdf downloaders), feel free to make Pull Requests!

---
