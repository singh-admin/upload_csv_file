import uvicorn
from fastapi import FastAPI, Request, File, UploadFile
from io import BytesIO
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
import pandas as pd
import sqlite3

app = FastAPI()

# point the directory template
templates = Jinja2Templates(directory="template")

# this function will render the html page where user can upload the CSV file.
@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


# this function used to upload the csv file and data will stored into the demo.db file. 
@app.post("/", response_class=HTMLResponse)
def upload(file: UploadFile=File(...)):
    content = file.file.read()
    # converting into byte format
    byte_data = BytesIO(content)
    data = pd.read_csv(byte_data)
    # removing the spackes from data (cleaning the datas).
    data.columns = data.columns.str.strip()
    # connects the sqlite3 database.
    connection = sqlite3.connect('csv.db')
    data.to_sql('csv_data', connection, if_exists='replace')
    connection.close()
    return "CSV data got upload into csv.db file you can see using the Sqlite Viewer!"




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")
