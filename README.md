# PDF Text Scraper

A Python desktop application that extracts text from multiple PDF files, including scanned PDFs using OCR.

I built this project while learning Python to practice working with graphical user interfaces, PDF processing, OCR, loops, functions, conditional logic, and file handling.

## Features

* Select one or multiple PDF files using a desktop interface
* Extract text from every page of each PDF
* Automatically detect when a page does not contain selectable text
* Use OCR to extract text from scanned PDF pages
* Handle PDFs containing a combination of text-based and scanned pages
* Save extracted text as a separate `.txt` file
* Automatically save the text file next to the original PDF

## Built With

* Python
* Tkinter
* PyPDF2
* PyMuPDF
* Pillow
* pytesseract
* Tesseract OCR

## How It Works

1. Run the Python application.
2. Click **Select PDFs**.
3. Select one or more PDF files.
4. Click **Extract Text**.
5. The program checks each page for embedded text.
6. If embedded text is available, PyPDF2 extracts it directly.
7. If no readable text is found, the page is converted to an image and processed with Tesseract OCR.
8. A `.txt` file is created next to each original PDF.

The application checks each page individually, so it can process PDFs containing both normal text pages and scanned pages.

## Installation

Clone the repository:

```bash
git clone https://github.com/kimsarsem/pdf-text-scraper.git
```

Move into the project folder:

```bash
cd pdf-text-scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required Python packages:

```bash
pip install PyPDF2 pytesseract PyMuPDF Pillow
```

## Install Tesseract OCR

The application also requires Tesseract OCR to process scanned PDFs.

On Windows, Tesseract can be installed using:

```powershell
winget install --id tesseract-ocr.tesseract
```

The application currently expects Tesseract to be installed at:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

## Run the Application

With the virtual environment activated, run:

```bash
python pdf_scraper.py
```

The PDF Text Scraper window will open.

Click **Select PDFs**, choose your PDF files, and then click **Extract Text**.

## OCR

For each PDF page, the application first attempts normal text extraction using PyPDF2.

If the page does not contain readable embedded text, the application:

1. Uses PyMuPDF to render the PDF page as an image.
2. Uses Pillow to handle the image in Python.
3. Sends the image to Tesseract through pytesseract.
4. Adds the recognized text to the output file.

OCR results may contain recognition errors depending on the quality, resolution, and formatting of the scanned document.

## Project Status

The application current
