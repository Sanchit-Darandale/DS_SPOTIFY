from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import search_spotify, download_youtube
from fastapi.responses import StreamingResponse
from pytube import Search
import requests
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(query: str = Query(...), type: str = Query("track")):
    try:
        return search_spotify(query, type)
    except Exception as e:
        return {"error": str(e)}

@app.get("/download")
async def download(query: str):
    from pytube import YouTube
    results = Search(query).results
    if not results:
        return {"error": "No video found"}
    video = results[0]
    stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
    if stream is None:
        return {"error": "No audio stream found"}
    audio_stream = requests.get(stream.url, stream=True)
    return StreamingResponse(audio_stream.iter_content(1024), media_type="audio/mp4")
