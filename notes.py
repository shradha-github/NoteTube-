from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app=FastAPI()

class Notes(BaseModel):
    title:str
    youtube_url:str
    notes:str

all_notes=[]    
@app.get("/")
def home():
    return {"Welcome to Home page"}

@app.post("/save")
def save(note:Notes):
    data={"title":note.title,
    "youtube_url":note.youtube_url,
    "notes":note.notes,
    "date":datetime.now()
    }
    all_notes.append(data)
    return {"Message":"Notes saved","data":data}

@app.get("/get")
def get():
    return all_notes











