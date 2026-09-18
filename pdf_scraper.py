from tkinter import Tk, Button, Label, filedialog
from PyPDF2 import PdfReader
import pymupdf
import pytesseract
from PIL import Image
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

selected_files = []

def select_pdfs():
    global selected_files

    selected_files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF files", "*.pdf")]
    )

    status_label.config(text=f"{len(selected_files)} PDF(s) selected")

def extract_text():
    for pdf_file in selected_files:
        reader = PdfReader(pdf_file)
        pdf_document = pymupdf.open(pdf_file)

        text = ""

        for page_number, page in enumerate(reader.pages):
            page_text = page.extract_text()

            if page_text and page_text.strip():
                text += page_text + "\n"

            else:
                pdf_page = pdf_document[page_number]

                pix = pdf_page.get_pixmap(
                    matrix=pymupdf.Matrix(2, 2)
                )

                image = Image.open(
                    BytesIO(pix.tobytes("png"))
                )

                ocr_text = pytesseract.image_to_string(image)

                text += ocr_text + "\n"

        pdf_document.close()

        output_file = pdf_file.replace(".pdf", ".txt")

        with open(output_file, "w", encoding="utf-8") as file:
            if text.strip():
                file.write(text)
            else:
                file.write(
                    "No readable text was found in this PDF.\n\n"
                    "The program attempted both normal text extraction "
                    "and OCR, but no text could be recognized."
                )

    status_label.config(
        text=f"Done! {len(selected_files)} PDF(s) processed."
    )

window = Tk()
window.title("PDF Text Scraper")
window.geometry("400x250")

title = Label(window, text="PDF Text Scraper")
title.pack(pady=20)

select_button = Button(window, text="Select PDFs", command=select_pdfs)
select_button.pack(pady=10)

extract_button = Button(window, text="Extract Text", command=extract_text)
extract_button.pack(pady=10)

status_label = Label(window, text="No PDFs selected")
status_label.pack(pady=10)

window.mainloop()