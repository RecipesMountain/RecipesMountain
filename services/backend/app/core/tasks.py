from sqlalchemy.orm.session import Session
from services.backend.app.schemas.recipe import RecipeSearch
from app.main import app
from fastapi_utils.tasks import repeat_every
from app.api import deps
from app import crud
from app.models.recipe import Recipe
from fastapi import Depends


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 24 * 4)  # every 4 days
def recalculatePopularity(db: Session = Depends(deps.get_db)) -> None:
    recipes = crud.recipe.get_all(db)
    for r in recipes:
        r.popularityScore = r.popularityScore / 2
        db.add(r)
    db.commit()
    # 99% it's not needed but i don't want to deal with stupid bugs letter on
    for r in recipes:
        db.refresh(r)
