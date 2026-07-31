import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def generate_resume(job_description, job_info, answers):
    interview_answers = ""

    for question, answer in answers.items():
        interview_answers += f"\nQuestion: {question}\nAnswer: {answer}\n"

    prompt = f"""
You are an expert ATS Resume Writer.

Write a professional, ATS-friendly resume based on:

JOB DESCRIPTION
----------------
{job_description}

EXTRACTED JOB INFORMATION
-------------------------
{job_info}

CANDIDATE ANSWERS
-----------------
{interview_answers}

Requirements:

- Use professional formatting.
- Include:
  • Professional Summary
  • Technical Skills
  • Professional Experience
  • Projects
  • Education
  • Certifications (if applicable)
- Quantify achievements whenever possible.
- Tailor the resume to the provided job description.
- Do not invent personal details such as name, phone number, or email.
- Use only the information provided by the candidate.
- Return plain text only.
"""

    response = client.chat.completions.create(
        model="inclusionai/ling-3.0-flash:free",
        messages=[
            {
                "role": "system",
                "content": "You are an expert ATS resume writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content.strip()