#import uvicorn
from fastapi import FastAPI
from typing import Union
from fastapi.responses import FileResponse, PlainTextResponse, JSONResponse, StreamingResponse, Response
from fastapi.middleware.cors import CORSMiddleware
import json
import tofile
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

@app.get("/check_ip/{ips_text}/", response_class=PlainTextResponse)
async def check_ip(ips_text: str):
    return ips_text

@app.get("/check_ip/{ips_text}/pdf", response_class=StreamingResponse)
async def check_ip(ips_text: str):
    data = json.load(open('example.json', 'r'))
    pdf_db = tofile.new_pdf(data)
    headers = {'Content-Disposition': 'inline; name="out_pdf"; filename="out.pdf"'}
    return Response(pdf_db, headers=headers, media_type='application/pdf')

@app.get("/check_ip/{ips_text}/csv")#, response_class=PlainTextResponse)
async def check_ip(ips_text: str):
    data = json.load(open('example.json', 'r'))
    csv_db = tofile.new_csv(data)
    headers = {'Content-Disposition': 'inline; name="out_csv"; filename="out.csv"'}
    return Response(csv_db, headers=headers, media_type='text/csv')