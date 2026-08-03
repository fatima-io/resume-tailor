from docx import Document


def create_docx(resume_text, output_path):

    doc = Document()

   

    for line in resume_text.split("\n"):
        doc.add_paragraph(line)

    doc.save(output_path)