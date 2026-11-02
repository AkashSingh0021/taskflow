from PyPDF2 import PdfReader

def extract_text(pdf_file):

    try:

        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

        return text

    except Exception:

        return "Unable to read PDF."