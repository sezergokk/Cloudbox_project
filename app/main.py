from fastapi import FastAPI, UploadFile, File, HTTPException
from app.supabase_client import upload_file_to_supabase  

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CloudBox API is running!"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        url = upload_file_to_supabase(contents, file.filename)
        return {"filename": file.filename, "url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

