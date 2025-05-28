from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, ValidationError
import random
import json

app = FastAPI()


class joke_data(BaseModel):
    joke: str


with open('data/jokes.json', 'r') as jsonfile:
    read = jsonfile.read()

jokes = json.loads(read)


@app.get('/')
async def docs():
    return RedirectResponse(url="/docs")


@app.get('/all')
async def get_all_dev_jokes():
    return {"dev jokes": jokes}


@app.get('/devjokes')
async def get_random_dev_jokes():
    return {"dev joke": random.choice(jokes)}


@app.get('/{id}')
async def get_specified_jokes(id: int):
    for i in jokes:
        if i['id'] == id:
            return {'joke': i}

    return {'joke': 'not found'}


@app.post('/addjoke')
async def add_joke(joke: joke_data):
    try:
        add = joke.dict()
        add['id'] = random.randrange(0, 100000)
        jokes.append(add)
        return {'joke': add, 'status': 'successfully added :)'}
    except ValidationError as e:
        return {'error': e}


@app.delete('/rmjoke/{id}')
async def delete_joke(id: int):
    for i in jokes:
        if i['id'] == id:
            jokes.pop(id - 1)
            return {'removed': i}
    return {'joke': 'not found'}
