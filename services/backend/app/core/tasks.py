from services.backend.app.schemas.recipe import RecpieSearch
from app.main import app
from fastapi_utils.tasks import repeat_every
from app.api import deps
from app import crud
from app.models.recipe import Recipe
from fastapi import Depends


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 8)
def recalculatePopularity(db=Depends(deps.get_db)) -> None:
    recpies = crud.recipe.get_all(db)
