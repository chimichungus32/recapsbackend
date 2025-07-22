from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transcribe import transcribe

app = FastAPI()

origins = [
    "http://172.31.96.178:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/transcription/youtube") # Fast api will get query parameer for you
async def return_transcription(url: str):
    if not url.startswith("https://www.youtube.com/watch?v="):
        raise HTTPException(status_code=400, detail="Invalid YouTube URL provided")

    transcription = await transcribe(url)
    return transcription