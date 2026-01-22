from fastapi import FastAPI, HTTPException, UploadFile

import uitils
import db
from mysql.connector import MySQLConnection

app = FastAPI()

manager = db.MySQLManager()
curser =  db.Init_sql(manager.get_cnx())

curser.create_table()

@app.post('/upload')
def upload_file(file: UploadFile):
    try:
        processing = uitils.Data_processing(file.file)
        info = curser.insert(processing)
        return {'massege': info}
    except HTTPException as e:
        return str(e)
    


