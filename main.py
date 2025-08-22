#Import nach PEP8 Standard -> Third Party -> Local Modules

import subprocess as sp
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import remote_functions as rmf


app = FastAPI()
# "static" Ordner für CSS, JS, Bilder
app.mount("/static", StaticFiles(directory="static"), name="static")

Buttons = {"rm1": rmf.rm1,
           "rm2": rmf.rm2,
           "rm3": rmf.rm3,
           "rm4": rmf.rm4,
           "rm5": rmf.rm5,
           "rm6": rmf.rm6,
           "rm7": rmf.rm7,
           "rm8": rmf.rm8
           }
BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = (BASE_DIR / "main.html").resolve()

@app.get("/", include_in_schema=True)
def home():
    return FileResponse(str(HTML_PATH))
#fügt den Rückgabe String in die Adresse Zeile an.

@app.get("/action/{name}")
def action(name: str):
    fn = Buttons.get(name)
    if not fn:
        return RedirectResponse("/", status_code=303)
    msg = fn()
    return RedirectResponse(f"/?ok={msg}", status_code=303)
