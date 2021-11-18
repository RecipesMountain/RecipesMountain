from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

__version__ = '0.1.0'

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"msg": "Hello World"}


def main():
    uvicorn.run('src:app', host='0.0.0.0', port=8080, reload=True)