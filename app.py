from flask import Flask, render_template, request, send_file
from utils.file_parser import parse_uploaded_file
from ai.analyzer import analyze_resume
from ai.resume_writer import generate_resume
from exporters.docx_export import create_docx

import tempfile

app = Flask(__name__)

# Storing the latest generated resume
latest_resume = ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    global latest_resume

    # Job Description

    job_description = request.form.get("job_description", "")

    job_file = request.files.get("job_file")

    if job_file and job_file.filename:
        job_description = parse_uploaded_file(job_file)


    # Resume

    resume_text = request.form.get("resume_text", "")

    resume_file = request.files.get("resume_file")

    if resume_file and resume_file.filename:
        resume_text = parse_uploaded_file(resume_file)


    # AI Analysis
    analysis = analyze_resume(job_description, resume_text)


    # AI Resume

    latest_resume = generate_resume(job_description, resume_text)

    return render_template(
        "result.html",
        analysis=analysis,
        resume=latest_resume
    )


@app.route("/download-docx")
def download_docx():

    global latest_resume

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")

    create_docx(latest_resume, temp.name)

    return send_file(
        temp.name,
        as_attachment=True,
        download_name="AI_Optimized_Resume.docx"
    )


if __name__ == "__main__":
    app.run(debug=True)