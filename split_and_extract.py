from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
import os
import re

def extract_registration(text):
    match = re.search(r'\b[A-Z]{1,3}-[A-Z]{1,2} \d{1,4}\b', text)
    if match:
        plate = match.group(0)
        if 8 <= len(plate) <= 10:
            return plate
    return "Not found"

def split_and_extract(input_path, output_folder, result_xlsx):
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    results = []

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(0, total_pages, 2):
        writer = PdfWriter()
        name = f"split_{i+1:03d}_{min(i+2, total_pages):03d}.pdf"
        out_file = os.path.join(output_folder, name)

        writer.add_page(reader.pages[i])
        if i + 1 < total_pages:
            writer.add_page(reader.pages[i+1])

        with open(out_file, "wb") as f_out:
            writer.write(f_out)

        text = reader.pages[i].extract_text()
        reg_number = extract_registration(text)
        results.append({"File": name, "Registration No": reg_number})

    df = pd.DataFrame(results)
    df.to_excel(result_xlsx, index=False)
