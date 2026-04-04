from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Model
class Notes(BaseModel):
    title: str
    youtube_url: str
    notes: str

# Temporary database
all_notes = []

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Home page"}

# Save notes
@app.post("/save")
def save(note: Notes):
    data = {
        "title": note.title,
        "youtube_url": note.youtube_url,
        "notes": note.notes,
        "date": str(datetime.now())
    }
    all_notes.append(data)
    return {"message": "Notes saved", "data": data}

# Get all notes
@app.get("/get")
def get_notes():
    return all_notes