import jinja2
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from app.dispatcher import main_router
#router_views = APIRouter()
#router_views.include_router()
# создаем функцию, которая будет отдавать html-файл
templates = Jinja2Templates(directory="public")

@main_router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@main_router.get("/popup1/", response_class=HTMLResponse)
async def read_item2(request: Request):
    return templates.TemplateResponse("popup1.html", {"request": request})

@main_router.get("/sing-up/", response_class=HTMLResponse)
async def read_item3(request: Request):
    return templates.TemplateResponse("sing_up.html", {"request": request})

@main_router.get("/sing-in/", response_class=HTMLResponse)
async def read_item4(request: Request):
    return templates.TemplateResponse("sing_in.html", {"request": request})


@main_router.get("/shop-online/", response_class=HTMLResponse)
async def read_item5(request: Request):
    return templates.TemplateResponse("shop-online.html", {"request": request})


@main_router.get("/gpt/", response_class=HTMLResponse)
async def read_item6(request: Request):
    return templates.TemplateResponse("gpt.html", {"request": request})


