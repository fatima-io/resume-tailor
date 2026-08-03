from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def generate_resume(job_description, resume):

    prompt = f"""
You are a professional ATS Resume Writer.

The user uploads:

1. Job Description
2. Existing Resume

Your job is to generate a brand new ATS-optimized resume.

Rules:

- Keep all information truthful.
- Improve wording.
- Rewrite the professional summary.
- Improve project descriptions.
- Improve experience.
- Add relevant keywords from the job description naturally.
- Keep the resume professional.
- Return ONLY the resume.

Job Description:

{job_description}

Resume:

{resume}
"""

    response = client.chat.completions.create(
        model="inclusionai/ling-3.0-flash:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content