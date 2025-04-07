from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/")
async def handle(question: str = Form(...), file: UploadFile = Form(...)):
    return JSONResponse({
        "question": question,
        "filename": file.filename
    })
