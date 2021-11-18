from typing import Any

from fastapi import APIRouter, Depends

from app import models, schemas

router = APIRouter()


@router.get("/test-db/", response_model=schemas.Msg, status_code=200)
def test_db() -> Any:
    return {"msg": "test db"}
