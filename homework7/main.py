from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_product, get_contacts

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {"request": request,
               "products": get_product()}
    return templates.TemplateResponse("index.html", context)


@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {"request": request,
               "products": get_product()}
    return templates.TemplateResponse("home.html", context)


@app.get("/settings", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("settings.html", context)


@app.get("/about", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {"request": request,
               "contacts": get_contacts()}
    return templates.TemplateResponse("about.html", context)
