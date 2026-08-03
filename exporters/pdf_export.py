from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(resume_text, output_path):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(output_path)

    story = []

    for line in resume_text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(line, styles["Normal"])
            )

    doc.build(story)