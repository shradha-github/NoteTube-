@app.post("/download_pdf")
def download_pdf(data:YouTubeRequest):
    video_id = extract_video_id(data.youtube_url)
    transcript = get_transcript(video_id)
    notes = generate_notes(transcript)
    file_path = create_pdf(notes)

    return FileResponse(file_path,media_type = "application/pdf",filename = "notes.pdf")