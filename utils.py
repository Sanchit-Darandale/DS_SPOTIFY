import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from yt_dlp import YoutubeDL

client_id = os.getenv("SPOTIFY_CLIENT_ID", "031cec83776147258a0bc6a4a9c258c6")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "f6faf8eb6e4a48449050732898f48c9a")

if not client_id or not client_secret:
    raise ValueError("Missing SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def search_spotify(query, type="track"):
    return sp.search(query=query, type=type, limit=1)

def download_youtube(query):
    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True,
        'noplaylist': True,
        'default_search': 'ytsearch',
    }
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(query, download=False)
        if 'entries' in result:
            result = result['entries'][0]
        return {"url": result['url']}
