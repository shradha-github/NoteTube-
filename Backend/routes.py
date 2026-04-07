#from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
from transcript import get_transcript
from ai import generate_notes
from helpers import extract_video_id

print("routes file loaded")
router = APIRouter()

class YouTubeRequest(BaseModel):
    youtube_url: str

@router.post("/generate-notes")
def generate_notes_api(data: YouTubeRequest):
    video_id = extract_video_id(data.youtube_url)

    if not video_id:
        return {"error": "Invalid YouTube URL"}

    transcript_text = get_transcript(video_id)

    if transcript_text == "No transcript available":
        return {"status": "error", "message": "No transcript available"}

    notes = generate_notes(transcript_text)

    return {
        "status": "success",
        "notes": notes
    }