from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn
import uitils
import db
from mysql.connector import MySQLConnection

app = FastAPI()

manager =  db.MySQLManager()
curser =  db.Init_sql( MySQLConnection)
cnx = manager.get_cnx()
curser.create_table()

@app.post('/upload')
def upload_file(file: UploadFile):
    processing = uitils.Data_processing(file.file)
    curser  = cnx.cursor()

    


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)    