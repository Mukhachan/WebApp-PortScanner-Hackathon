from fastapi import FastAPI
from typing import Union
from fastapi.responses import FileResponse
 
app = FastAPI()
 
@app.get("/")
def root():
    return {"message": "Momento mori"}



@app.get("/check_ip/{ips_text}/", response_class=FileResponse)
def check_ip(ips_text: int):
    return FileResponse("images.jpeg")
    