from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api.api import api_router
from app.core.config import settings

__version__ = "0.1.0"

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
def home():
    return {"msg": "Hello World"}


app.include_router(api_router, prefix=settings.API_V1_STR)


def uvicorn_main():
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
