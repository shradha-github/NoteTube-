from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1"
)

def generate_notes(transcript_text):
    if transcript_text ==None  or len(transcript_text.strip()) < 50:
        return "Transcript not available to convert into notes."

    transcript_text = transcript_text[:3000]

    prompt = f"""
You are a notes-making assistant.

Convert this YouTube transcript into clean student notes.

Rules:
- Use simple English
- Keep technical terms
- Use headings starting with ##
- Use bullet points with -
- Short sentences
- Do NOT ask questions

Transcript:
{transcript_text}
"""

    response = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {"role": "system",
             "content": "You convert transcripts into student notes."},
            {"role": "user",
             "content": prompt}
        ]
    )

    return response.choices[0].message.content