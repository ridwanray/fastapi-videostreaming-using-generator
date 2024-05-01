from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
import os

VIDEO_FILE = "video.mp4"
CHUNK_SIZE = 1024 * 1024

app = FastAPI(title="Video Streaming")
templates = Jinja2Templates(directory="templates")


def generate_video_chunks():
    with open(VIDEO_FILE, "rb") as file_object:
        counter = 0
        while True:
            chunk = file_object.read(CHUNK_SIZE)
            if not chunk:
                print("End of chunks")
                break  # "abcdef"
            counter = counter + 1
            print("Chunk Counter", counter)
            yield chunk


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", context={"request": request, "title": "FastAPI Video Streaming"}
    )


@app.get("/stream-video")
async def stream_video(request: Request):
    file_size = os.stat(VIDEO_FILE).st_size
    headers = {
        "content-type": "video/mp4",
        "accept-ranges": "bytes",
        "content-encoding": "identity",
        "content-length": str(file_size),
        "content-range": f"bytes 0-{file_size-1}/{file_size}",
    }
    return StreamingResponse(
        content=generate_video_chunks(),
        headers=headers,
        status_code=status.HTTP_206_PARTIAL_CONTENT,
        media_type="video/mp4",
    )
