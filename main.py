from fastapi import FastAPI

app = FastAPI(
    description='Online Bibliothek'
)


@app.get('/')
def index():
    return {'status': 200}