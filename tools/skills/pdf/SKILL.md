---
name: pdf
description: Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging, splitting, and form handling.
---

# PDF Processing

## Python Libraries

### pypdf
Basic operations: read, merge, split, metadata, rotation
```python
from pypdf import PdfReader
reader = PdfReader("file.pdf")
for page in reader.pages:
    print(page.extract_text())
```

### pdfplumber
Text and table extraction with layout preservation
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())
        tables = page.extract_tables()
```

### reportlab
Create PDFs from scratch
```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
c = canvas.Canvas("output.pdf", pagesize=letter)
c.drawString(100, 750, "Hello World")
c.save()
```

## Command-Line Tools

- `pdftotext` - Extract text
- `qpdf` - Merge, split, decrypt
- `pdftk` - Form filling, metadata

## Common Tasks

| Task | Tool |
|------|------|
| Extract text | pdfplumber, pdftotext |
| Merge PDFs | pypdf, qpdf |
| Split pages | pypdf, qpdf |
| Extract tables | pdfplumber |
| Create new | reportlab |
| OCR scanned | pytesseract |
| Fill forms | pdftk |
