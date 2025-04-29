from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
from utils import extract_lab_tests

# For Mac with Homebrew-installed Tesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

app = FastAPI()

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        text = pytesseract.image_to_string(image)
        lab_tests = extract_lab_tests(text)
        return JSONResponse(content={"is_success": True, "data": lab_tests})
    except Exception as e:
        return JSONResponse(content={"is_success": False, "error": str(e)})
