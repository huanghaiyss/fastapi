from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import shutil
from split_logic import split_file_by_keyword
import uuid

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/split")
async def split_file(keyword: str = Form(...), file: UploadFile = Form(...)):
    # Generate unique folder ID for results
    unique_id = str(uuid.uuid4())
    result_dir = os.path.join("static", "results", unique_id)
    os.makedirs(result_dir, exist_ok=True)

    # Save uploaded file temporarily
    temp_input_path = os.path.join(result_dir, file.filename)
    with open(temp_input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Split file
    split_file_by_keyword(temp_input_path, result_dir, keyword)

    # Redirect to result page
    return RedirectResponse(url=f"/results/{unique_id}", status_code=302)


@app.get("/results/{uid}", response_class=HTMLResponse)
async def show_results(request: Request, uid: str):
    result_path = os.path.join("static", "results", uid)
    if not os.path.isdir(result_path):
        return HTMLResponse(content="Result not found", status_code=404)

    files = os.listdir(result_path)
    files = [f"/static/results/{uid}/{f}" for f in files if not f.startswith(".")]

    return templates.TemplateResponse("results.html", {
        "request": request,
        "files": files,
        "uid": uid
    })