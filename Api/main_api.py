#import uvicorn
from fastapi import FastAPI
from typing import Union
from fastapi.responses import FileResponse, PlainTextResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
#import Core.logic
 
app = FastAPI()
 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=JSONResponse)
def root():
    data = json.load(open('example.json', 'r'))
    return JSONResponse(content=data)



#@app.get("/check_ip/{ips_text}/", response_class=PlainTextResponse)
#async def check_ip(ips_text: int):
#    return ips_text

#@app.get("/check_ip/{ips_text}/pdf", response_class=FileResponse)
#async def check_ip(ips_text: int):
#    return FileResponse("test.pdf")
