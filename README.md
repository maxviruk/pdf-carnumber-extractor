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
- 📁 Keeps only system folders (`sample_data`, `.config`) and `.ipynb` file

---

## 🚀 How to Use It

1. Open the notebook in **Google Colab**:
   [![Open In Colab]([https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maxviruk/pdf-carnumber-extractor/blob/main/pdf_extractor_final_cleaned.ipynb](https://colab.research.google.com/github/maxviruk/pdf-carnumber-extractor/blob/main/pdf_extractor_final_cleaned.ipynb
)

2. **Upload your PDF** using the provided cell

3. The script will:
   - Clear previously generated files
   - Split the PDF into 2-page parts
   - Extract car numbers like `B-AB 1234`, `HB-AA 4567`, etc.
   - Save split PDFs to `/splits` and generate `result.xlsx`
   - Archive the splits into `split_files.zip`

4. **Download** the Excel file and ZIP with all chunks

---

## 🧪 Plate Format Example

```text
B-AB 1234
```

Regex pattern used:

```python
\b[A-Z]{1,3}-[A-Z]{1,2} \d{1,4}\b
```

---

## 📁 Output Files

- `/splits/*.pdf` – split files named by car number or fallback
- `result.xlsx` – summary Excel
- `split_files.zip` – archive with all PDF chunks

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

