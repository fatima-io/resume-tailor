from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def analyze_resume(job_description, resume):

    prompt = f"""
You are an ATS Resume Expert.

Analyze the resume against the job description.

Return ONLY the following sections.

ATS Score:
(A score out of 100)

Matched Skills:
(Bullet list)

Missing Skills:
(Bullet list)

Suggestions:
(Numbered list)

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