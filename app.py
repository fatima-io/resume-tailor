from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    job_description = request.form.get("job_description")

    job_file = request.files.get("job_file")

    resume_file = request.files.get("resume_file")

    print(job_description)
    print(job_file)
    print(resume_file)

    return "Files received successfully!"


if __name__ == "__main__":
    app.run(debug=True)