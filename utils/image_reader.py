import easyocr
import tempfile

reader = easyocr.Reader(["en"])

def read_image(file):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
        file.save(temp.name)

        result = reader.readtext(temp.name)

    text = ""

    for item in result:
        text += item[1] + " "

    return text