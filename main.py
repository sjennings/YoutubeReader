# YouTube Transcript Downloader

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

video_url = input("Enter the video url: ")
video_title = input("Enter the video title: ")
_id = video_url.split("=")[1].split("&")[0]

transcript = YouTubeTranscriptApi.get_transcript(_id)
fmt = TextFormatter()
text_formatted = TextFormatter.format_transcript(fmt, transcript)
text_file_title = video_title + ".txt"
with open(text_file_title, 'w', encoding='utf-8') as text_file:
    text_file.write(text_formatted)
