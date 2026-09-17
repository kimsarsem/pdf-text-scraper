# PDF Text Scraper

A simple Python desktop application that extracts text from multiple PDF files.

I built this project while learning Python to practice working with graphical user interfaces, PDF processing, loops, functions, conditional logic, and file handling.

## Features

- Select one or multiple PDF files using a desktop interface
- Extract text from every page of each PDF
- Save extracted text as a separate `.txt` file
- Automatically save the text file next to the original PDF
- Detect PDFs that do not contain readable text
- Explain when a PDF may require OCR

## Built With

- Python
- Tkinter
- PyPDF2

## How It Works

1. Run the Python application.
2. Click **Select PDFs**.
3. Select one or more PDF files.
4. Click **Extract Text**.
5. A `.txt` file is created for each PDF.

If a PDF contains scanned images instead of selectable text, the program explains that OCR may be required.

## Installation

Clone the repository:

```bash
git clone https://github.com/kimsarsem/pdf-text-scraper.git