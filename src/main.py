from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .services.swapi import SwApi

app = FastAPI(
    title="StarWarsAPI",
    version="0.0.1",
)


@app.get("/", response_class=HTMLResponse)
async def home():
    return "<html>Visit <a href=\"http://127.0.0.1:8000/docs\">swagger documentation</a></html>"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/starships")
async def get_starships(asc: bool = False, sort_by: str = "name"):
    api = SwApi()
    return api.get_starships(asc, sort_by)

