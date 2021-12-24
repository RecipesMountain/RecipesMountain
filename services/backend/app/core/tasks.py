from services.backend.app.schemas.recipe import RecpieSearch
from app.main import app
from fastapi_utils.tasks import repeat_every
from app.api import deps
from app import crud
from app.models.recipe import Recipe

@app.on_event("startup")
@repeat_every(seconds=60*60*8) 
def recalculatePopularity() -> None:
    db = deps.get_db() #pls work
    recpies = crud.recpie.get_all(db)

    for r in recpies:
        r.popularityScore = 4*abs(0.2 - r.viewsLast24 /total)*r.popularityScore
        crud.recpie.update(db, db_obj=Recipe, obj_in=r )
