# 🚗 PDF Car Number Extractor

This Google Colab notebook helps you:
1. Split a multi-page PDF into 2-page chunks
2. Extract car registration numbers from the first page of each chunk
3. Rename each chunk using the registration number (or mark as Not found)
4. Export all results to an Excel file
5. Download all split PDFs as a ZIP file

---

## ✅ What’s New
- 🧹 Automatically deletes all previously generated files (PDFs, Excel, ZIP) before processing
- 🧠 Extracted plate numbers are now filtered by:
  - Valid format (e.g., `B-AB 1234`)
  - Correct length (8 to 10 characters)
  - Strict end check: avoids trailing digits like `3466` when real plate is `346`

---

## 🚀 How to Use It

1. Open the notebook in **Google Colab**:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maxviruk/pdf-carnumber-extractor/blob/main/pdf_extractor_final_cleaned_v3.ipynb)

2. **Upload your PDF** using the provided cell

3. The script will:
   - Clear previously generated files
   - Split the PDF into 2-page parts
   - Extract car numbers like `B-AB 1234`, `HB-AA 4567`, etc.
   - Reject plates that are too short, too long, or have extra digits
   - Save split PDFs to `/splits` and generate `result.xlsx`
   - Archive the splits into `split_files.zip`

4. **Download** the Excel file and ZIP with all chunks

---

## 🧪 Plate Format Example

```text
HB-AA 346
```

Regex pattern used:

```python
\b[A-Z]{1,3}-[A-Z]{1,2} \d{1,4}(?!\d)
```

✅ Matches:
- `HB-AA 346` (OK)

❌ Does not match:
- `HB-AA 3466` (Too long)
- `HB-AA 34` (Too short)

---

## 📁 Output Files

| File Name           | Registration No |
|---------------------|-----------------|
| HB_AB_4567.pdf      | HB-AB 4567      |
| Not_found_003.pdf   | Not found       |

---

## 🛠️ Dependencies

```bash
PyPDF2
pandas
openpyxl
```

(Installed automatically in Colab)
