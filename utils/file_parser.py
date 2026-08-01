import os

from utils.pdf_reader import read_pdf
from utils.docx_reader import read_docx
from utils.text_reader import read_txt
from utils.image_reader import read_image


def parse_uploaded_file(file):

    filename = file.filename.lower()

    ext = os.path.splitext(filename)[1]

    if ext == ".pdf":
        return read_pdf(file)

    elif ext == ".docx":
        return read_docx(file)

    elif ext == ".txt":
        return read_txt(file)

    elif ext in [".png", ".jpg", ".jpeg"]:
        return read_image(file)

    else:
        return ""