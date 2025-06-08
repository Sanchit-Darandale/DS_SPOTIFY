from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import search_spotify, download_youtube

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
    try:
        return search_spotify(q, type)
    except Exception as e:
        return {"error": str(e)}

@app.get("/download")
def download(query: str):
    try:
        return download_youtube(query)
    except Exception as e:
        return {"error": str(e)}
      
