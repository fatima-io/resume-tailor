import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def analyze_job_desc(job_desc):
    prompt = f"""
You are an expert HR recruiter.

Analyze the following job description.

Return ONLY valid JSON using this exact format:

{{
    "Job Title": "",
    "Company": "",
    "Location": "",
    "Employment Type": "",
    "Experience": "",
    "Education": "",
    "Required Skills": [],
    "Preferred Skills": [],
    "Responsibilities": [],
    "Keywords": []
}}

Job Description:
{job_desc}
"""

    response = client.chat.completions.create(
        model="inclusionai/ling-3.0-flash:free",
        messages=[
            {
                "role": "system",
                "content": "You extract structured information from job descriptions and respond only with valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}") + 1

        if start != -1 and end != -1:
            return json.loads(content[start:end])

        raise Exception("The AI returned invalid JSON.")