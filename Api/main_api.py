#import uvicorn
from fastapi import FastAPI
from typing import Union
from fastapi.responses import FileResponse, PlainTextResponse
#import Core.logic
 
app = FastAPI()
 
@app.get("/", response_class=FileResponse)
def root():
    return FileResponse("example.json")



#@app.get("/check_ip/{ips_text}/", response_class=PlainTextResponse)
#async def check_ip(ips_text: int):
#    return ips_text

#@app.get("/check_ip/{ips_text}/pdf", response_class=FileResponse)
#async def check_ip(ips_text: int):
#    return FileResponse("test.pdf")
