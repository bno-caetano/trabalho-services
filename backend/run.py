from tokenize import Token
from core.video_transcript import Transcript
from core.text_completion import *
from utils.count_tokens import TokenCount
from core.text_completion import TextCompletion
from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import contextmanager

## Transcreve video do youtube

# url = "https://www.youtube.com/watch?v=aMIt_ON4CKk" # meu timao
# url = "https://www.youtube.com/watch?v=N7_z3GABxho" # dep
url = "https://www.youtube.com/watch?v=Xv_KGUqPyx0" # canal do tf

app = FastAPI()

@app.get("/")
async def init():
    return {"message":"hello world"}

@app.get("/yt_transcript/")
async def yt_trancript(url:str):
    yt_transcript = Transcript()

    id = yt_transcript.get_yt_id(url)
    transcript = yt_transcript.transcript_from_id(id)
    formatted_output = yt_transcript.format_transcript(transcript)

    return {"message":formatted_output}

# Define quantidade de tokens a serem reprocessados

@app.get("/tokens/")
async def tokens_proc(txt:str):
    tokens = TokenCount()
    num_token = tokens.count_tokens(txt)

    print('quantidade de tokens a serem processados:', num_token)
    
    return {"message":num_token}

@app.post("/response/")
async def completion(prompt:str, num_token:int, key:str):
    print('post prompt', prompt)
    comp = TextCompletion(prompt=prompt, num_token=num_token, key=key)
    response = comp.final_response()
    
    return response
          