from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn

app = FastAPI()

@app.post('/upload')
def upload_file(file: UploadFile):
    print(file)


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)    