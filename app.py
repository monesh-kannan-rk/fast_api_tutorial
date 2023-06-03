from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"data": {"hi": "hola"}}


@app.get('/about')
def about():
    return {"data": {"hi": "data"}}
