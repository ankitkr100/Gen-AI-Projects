from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    video_id = video_url.split("v=")[-1].split("&")[0]
    
    try:
        ytt_api = YouTubeTranscriptApi()          # ✅ create instance
        fetched = ytt_api.fetch(video_id)          # ✅ use .fetch()
        
        text_transcript = " ".join([entry.text for entry in fetched])
        return text_transcript
    
    except Exception as e:
        return f"An error occurred: {e}"

video_url = "https://www.youtube.com/watch?v=l00VBUXl1Q4"
print(get_youtube_transcript(video_url))