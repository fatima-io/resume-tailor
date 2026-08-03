from flask import Flask, render_template, request
from utils.file_parser import parse_uploaded_file
from ai.analyzer import analyze_resume
from ai.resume_writer import generate_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():


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

    analysis = analyze_resume(
        job_description,
        resume_text
    )


    # AI Resume Generation

    optimized_resume = generate_resume(
        job_description,
        resume_text
    )

 
    # Show Result Page

    return render_template(
        "result.html",
        analysis=analysis,
        resume=optimized_resume
    )


if __name__ == "__main__":
    app.run(debug=True)