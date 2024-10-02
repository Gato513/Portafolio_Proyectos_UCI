from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#! Configura las rutas para archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
#! Configura Jinja2
templates = Jinja2Templates(directory="templates")

#! Definir Rutas de Sesion:
@app.get("/sign-in.html")
async def sign_in(request: Request):
    return templates.TemplateResponse("sign-in.html", {"request": request})

@app.get("/sign-up.html")
async def sign_up(request: Request):
    return templates.TemplateResponse("sign-up.html", {"request": request})

#?==================================================================================

#! Definir Rutas Principales:
@app.get("/")
async def inicio(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/dashboard.html")
async def inicio(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/tables.html")
async def tables(request: Request):
    return templates.TemplateResponse("tables.html", {"request": request})

@app.get("/billing.html")
async def billing(request: Request):
    return templates.TemplateResponse("billing.html", {"request": request})

@app.get("/profile.html")
async def rtl(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})


