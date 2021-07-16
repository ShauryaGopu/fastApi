from fastapi import FastAPI
#from pydantic import BaseModel

import pyqrcode
import io
from starlette.responses import StreamingResponse
import png
app = FastAPI()

@app.get('/')
def first():
    return {
        'message':'I am doing it 😁'
    }

@app.post("/image")
def qrCodeImage(stringInp):
    qrcode2 = pyqrcode.create(stringInp)
    #return StreamingResponse(io.BytesIO(qrcode2.tobytes()), media_type="image/png")
    qrcode2.png("myqr.png",scale=8)
    val=open("myqr.png", mode="rb")
    return StreamingResponse(val, media_type="image/png")
