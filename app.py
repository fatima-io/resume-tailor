from flask import Flask, render_template, request
from utils.file_parser import parse_uploaded_file

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    job_description = request.form.get("job_description")

    job_file = request.files.get("job_file")

    resume_file = request.files.get("resume_file")

    resume_text = ""

    if resume_file and resume_file.filename != "":
        resume_text = parse_uploaded_file(resume_file)

    print("========== JOB DESCRIPTION ==========")
    print(job_description)

    print("========== RESUME ==========")
    print(resume_text)

    return "Files received successfully!"


if __name__ == "__main__":
    app.run(debug=True)