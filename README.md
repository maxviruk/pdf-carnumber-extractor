# 🚗 PDF Car Number Extractor

This tool splits a multi-page vehicle-related PDF into 2-page chunks and extracts car registration numbers from the **first page** of each chunk.

✅ Fully runs in **Google Colab** — no installation required.

---

## ▶️ Open in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maxviruk/pdf-carnumber-extractor/blob/main/pdf_extractor.ipynb)

---

## 📋 What the script does

### 1. Upload a PDF
- Use the built-in file upload to add your full PDF.

### 2. Split the PDF
- The file is split into chunks of 2 pages.
- Each chunk is saved in a folder `splits/`.

### 3. Extract registration numbers
- The script looks for registration numbers on the **first page** of each 2-page chunk.
- Example formats detected: `B-AB 1234`, `D-XY 987`, etc.

### 4. Name files by plate number
- Files are saved using the detected plate number as the filename:
  - `B_AB_1234.pdf`, `D_XY_987.pdf`, etc.
- If no number is found, file is named like:
  - `Not_found_001.pdf`, `Not_found_003.pdf`, etc.

### 5. Generate Excel report
- An Excel file `result.xlsx` is created with:

| File name         | Registration No |
|-------------------|------------------|
| B_AB_1234.pdf     | B-AB 1234        |
| Not_found_003.pdf | Not found        |

### 6. Download the result
- The notebook downloads `result.xlsx` to your computer automatically.

---

## 📁 Output structure

```
splits/
├── B_AB_1234.pdf
├── Not_found_003.pdf
...
result.xlsx
```

---

## 🧑‍💻 How to use

1. Click the **"Open in Colab"** button above.
2. Upload your PDF file.
3. Run all cells.
4. Download the Excel summary and PDF chunks.

---
