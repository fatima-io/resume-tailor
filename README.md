# AI Resume Builder

An AI-powered Resume Builder that analyzes a job description, interviews the user, and generates an ATS-friendly resume using the OpenAI API.

## Features

- Analyze any job description
- Extract:
  - Job Title
  - Skills
  - Responsibilities
  - Experience
  - Education
- Generate interview questions
- Collect candidate answers
- Generate an ATS-friendly resume
- Export to:
  - Resume.docx
  - Resume.txt

## Project Structure

```
AI Resume Builder/
│
├── app.py
├── job_analyzer.py
├── questions_generator.py
├── interview.py
├── resume_writer.py
├── exporter.py
├── requirements.txt
├── README.md
├── .env
└── venv/
```

## Installation

Create a virtual environment

```
python -m venv venv
```

Activate it

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file

```
OPENAI_API_KEY=your_api_key_here
```

## Run

```
python app.py
```

## Workflow

1. Paste a job description.
2. AI extracts important information.
3. Interview questions are generated.
4. User answers the questions.
5. AI creates an ATS-friendly resume.
6. Resume is saved as:
   - Resume.docx
   - Resume.txt

## Technologies

- Python
- OpenAI API
- python-docx
- python-dotenv

## Future Improvements

- PDF Export
- Streamlit Web App
- Resume Scoring
- Cover Letter Generator
- LinkedIn Profile Generator
- Multi-language Support