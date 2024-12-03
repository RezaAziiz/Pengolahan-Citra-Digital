from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Template dan folder video
templates = Jinja2Templates(directory="templates")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")

# Data video (dinamis, membaca file dari folder "videos")
VIDEO_FOLDER = "videos"
videos = [{"title": file, "url": f"/videos/{file}"} for file in os.listdir(VIDEO_FOLDER) if file.endswith(".mp4")]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "videos": videos})

@app.get("/videos/{video_name}")
async def serve_video(video_name: str):
    video_path = os.path.join(VIDEO_FOLDER, video_name)
    if os.path.exists(video_path):
        return FileResponse(video_path)
    return {"error": "Video not found"}
