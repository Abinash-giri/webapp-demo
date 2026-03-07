from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio

app = FastAPI(title="Dynamic Profile App")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/skills", response_class=HTMLResponse)
async def skills(request: Request):
    return templates.TemplateResponse("skills.html", {"request": request})

@app.post("/feedback")
async def submit_feedback(
    name: str = Form(...),
    email: str = Form(...),
    suggestion: str = Form(...)
):
    # Later this will go to DB / S3 / DynamoDB
    print(name, email, suggestion)
    #await asyncio.sleep(5)  # Simulate async processing

    return {
        "message": "Feedback submitted successfully"
    }


@app.get("/feedback-form", response_class=HTMLResponse)
async def feedback_form(request: Request):
    return templates.TemplateResponse("feedback_form.html", {"request": request})


@app.get("/blocking")
def blocking_operation():
    import time
    time.sleep(5)  # Simulate a blocking operation
    return {"message": "Blocking operation completed"}


@app.get("/non-blocking")
async def non_blocking_operation():
    await asyncio.sleep(5)  # Simulate a non-blocking operation
    return {"message": "Non-blocking operation completed"}
