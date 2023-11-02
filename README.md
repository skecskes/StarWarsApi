# Star Wars API

## Task

I’d like you to create an API which provides ordered information on various entities from the Star Wars films by their statistics.

For the purpose of this task, you will use [SWAPI](https://swapi.dev/), a public Star Wars REST API.

Service should present an API which:

- Surfaces a list of starships sorted by name
- Allow the sort order to be ascending or descending
- Allow the sort key to be changed (e.g. sort by length or cost rather than name)

## Local dev

Create project specific environment for dependencies

    python3 -m venv .venv

Activate project libraries:

    source .venv/bin/activate

Install all project dependencies:

    pip install -r requirements.txt

Run the app

    uvicorn src.main:app --reload 


***Swagger available at http://127.0.0.1:8000/docs#/***