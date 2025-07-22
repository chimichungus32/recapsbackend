from typing import Union
from fastapi import FastAPI
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

@app.get("/transcription/youtube/{url}")
async def return_transcription(url: str):
    transcription = await transcribe(url)
    return transcription