from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn
import uitils
app = FastAPI()


@app.post('/upload')
def upload_file(file: UploadFile):
    processing = uitils.Data_processing(file.file)
    
    


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)    