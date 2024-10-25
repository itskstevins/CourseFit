import pdfplumber
from pprint import pprint
import pandas as pd
# Path to your PDF file
pdf_path = "C:/Users/0day/Downloads/Documents/cutoffs.pdf"
pdf = pdfplumber.open(pdf_path)

page = pdf.pages[0]

table_data = page.extract_tables()

#pprint(table_data)

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages
        data = []
        for page in pages:
            table = page.extract_table()
            if table:
                data.extend(table)
    return data


def save_to_excel(data, excel_path):
    df = pd.DataFrame(data)
    df.to_csv(excel_path, index=False)


if __name__ == "__main__":
    pdf_path = "C:/Users/0day/Downloads/Documents/cutoffs.pdf"
    excel_path = 'test.csv'

    extracted_data = extract_table_from_pdf(pdf_path)
    save_to_excel(extracted_data, excel_path)
