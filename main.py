from pypdf import PdfReader
import re

with open('buzzwords.txt', 'r') as scan:
    BUZZWORDS = [line.strip() for line in scan]




def pdfToText(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def buzzwordChecker(pdf):
    buzzwordCount = 0
    for word in BUZZWORDS:
        if re.search(fr"\b{word}\b", pdf, re.IGNORECASE):
            buzzwordCount += 1
            print(f"Found buzzword: {word}")
    if buzzwordCount == 0:
        print("No Buzzwords have been found in this CV")

path = r'PDF-Path'
text = pdfToText(path)
buzzwordChecker(text)