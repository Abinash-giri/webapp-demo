from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Dynamic Profile App")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/feedback")
async def submit_feedback(
    name: str = Form(...),
    email: str = Form(...),
    suggestion: str = Form(...)
):
    # Later this will go to DB / S3 / DynamoDB
    print(name, email, suggestion)

    return {
        "message": "Feedback submitted successfully"
    }
