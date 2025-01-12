from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="api/frontend/staticfiles"), name="static")

templates = Jinja2Templates(directory="api/frontend/templates")

print()


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="main.html")


@app.get("/lajak")
def lajak():
    return {"message": "I Love you Kajal"}
