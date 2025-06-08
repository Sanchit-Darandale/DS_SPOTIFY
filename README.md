# DS Spotify Dashboard 🎧

A web dashboard to search Spotify songs, preview them, and download audio via YouTube.

## Features
- Search Spotify for tracks, playlists, or albums
- Web playback of 30s previews
- Download track audio using YouTube (yt-dlp)

## Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Env Setup
Create `.env` file in backend:
```
SPOTIFY_CLIENT_ID=your_id
SPOTIFY_CLIENT_SECRET=your_secret
```
And `.env` in frontend:
```
VITE_API_URL=https://your-backend-service.onrender.com
```

## Deployment
- **Frontend**: Deploy on Vercel
- **Backend**: Deploy on Render using `render.yaml`
- 
