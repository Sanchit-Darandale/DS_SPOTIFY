from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import search_spotify, download_youtube
from fastapi.responses import StreamingResponse
from pytube import Search
import requests, os, io, yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(q: str = Query(...), type: str = Query("track")):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "default_search": "ytsearch",
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(q, download=False)
        if "entries" in info:
            info = info["entries"][0]
        stream_url = info["url"]

    def stream_audio():
        r = requests.get(stream_url, stream=True)
        for chunk in r.iter_content(1024):
            yield chunk

    return StreamingResponse(stream_audio(), media_type="audio/mpeg")
    
@app.get("/download")
async def download(query: str):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
        "extract_flat": "in_playlist",
        "default_search": "ytsearch",
        "forcejson": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        url = info['url']

    def generate():
        with requests.get(url, stream=True) as r:
            for chunk in r.iter_content(chunk_size=8192):
                yield chunk

    return StreamingResponse(generate(), media_type="audio/mpeg")
