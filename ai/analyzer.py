from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def analyze_resume(job_description, resume):

    prompt = f"""
You are an ATS Resume Expert.

Compare the following resume with the job description.

Return your answer in the following format:

ATS Score:
Matched Skills:
Missing Skills:
Suggestions:
Optimized Professional Summary:

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