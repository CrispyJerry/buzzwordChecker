from pypdf import PdfReader

def pdfToText(pdf):
    reader = PdfReader(pdf)
    
    page = reader.pages[0]
    
    text = page.extract_text()
    print(text)


path = r'PDF-DirectoryPath'
pdfToText(path)