import easyocr
import tempfile

def read_image(file):

    reader = easyocr.Reader(["en"])

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
        file.save(temp.name)

        result = reader.readtext(temp.name)

    text = ""

    for item in result:
        text += item[1] + " "

    return text