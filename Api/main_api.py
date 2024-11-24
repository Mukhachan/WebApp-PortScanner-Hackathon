#import uvicorn
import time
from typing import List, Annotated
from fastapi import Query
from fastapi import FastAPI, Request, Depends, Body
from fastapi import FastAPI, UploadFile, File
from typing import Union
from fastapi.responses import FileResponse, PlainTextResponse, JSONResponse, StreamingResponse, Response
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
import tofile
import os

import sys
sys.path.append("../")

from Core.logic import nmap_A_scan
from config import db_connect

app = FastAPI()
ip_port_API = "http://127.0.0.1:8000/"

#connection_DB = db_connect

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CheckIPParams(BaseModel):
    info_type: str
    body: bytes

class Banner(BaseModel):
    file: bytes
    body: dict

@app.get("/ip/{ipt}")
async def ip_get(ipt: str):
    data = nmap_A_scan(ipt)
    #data = json.load(open('example.json', 'r', encoding="utf-8"))
    data["pdf_report"] = f"{ip_port_API}get_pdf/{len(os.listdir('pdfs'))}.pdf"
    return JSONResponse(content=data)


@app.post("/file/")
async def file_post(file: bytes = File()):
    print(1)
    print(file)


@app.get("/check_ip/{ips_text}/", response_class=PlainTextResponse)
async def check_ip(ips_text: str):
    data = json.load(open('example.json', 'r'))
    name = tofile.new_pdf(data)
    
    
@app.get("/get_pdf/{ips_text}/", response_class=FileResponse)
async def checked_get_pdf(ips_text: str):
    if ips_text in os.listdir('pdfs'):
        path = f"pdfs/{ips_text}"
        headers = {'Content-Disposition': 'inline; name="out_pdf"; filename="out.pdf"'}
        return FileResponse(path, headers=headers, media_type='application/pdf')

@app.get("/get_file_csv/{ips_text}/")
async def checked_get_csv(ips_text: str):
    pass
    #data = json.load(open('example.json', 'r'))
    #data = []
    #for i in range()
    #csv_db = tofile.new_csv(data)
    #headers = {'Content-Disposition': 'inline; name="out_csv"; filename="out.csv"'}
    #return Response(csv_db, headers=headers, media_type='text/csv')