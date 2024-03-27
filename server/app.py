from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import csv
import datetime

from .models import LanguageChoice, QuestionChoice
from .helper import execute

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_methods=['*'],
	allow_headers=['*'],
	allow_credentials=True,
)

@app.post("/submit")
def submit(
    code: UploadFile,
    team_code: str = Form(...),
    question: QuestionChoice = Form(...),
    language: LanguageChoice = Form(...)
):
    binary_code_content = code.file.read()
    result = execute(language,question,binary_code_content).strip()
    
    with open('results.csv',"a") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(),team_code,question,language,result])

    return result

@app.post("/result")
def result(
    password: str = Form(...)
):
    if password == "solla maaten":
        return FileResponse('results.csv')
    return "You are Not authorized"