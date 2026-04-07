from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        for transcript in transcript_list:
            data = transcript.fetch()

            text = ""
            for t in data:   
                text += t.text + " "  
            return text

        return "No transcript available"

    except Exception as e:
        print("Transcript error:", str(e))
        #return "No transcript available"

