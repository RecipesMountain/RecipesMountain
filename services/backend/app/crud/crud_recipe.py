from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.functions import func

from app.crud.base import CRUDBase
from app.models.recipe import Recipe
from app.models.tag import Tag

from app.schemas.recipe import RecipeCreate, RecipeUpdate


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):    
    def get_by_tags_and(self, db: Session, *, tags: List[Recipe]) -> List[Recipe]:
        q = db.query(Recipe)
        for tag in tags:
            q = q.filter(Recipe.tags.any(tag.name.contains(tag)))
        return q.all()

    # def get_by_tags_or(self, db: Session, *, tags: List[Recipe]) -> List[Recipe]:
    #     q = db.query(Recipe)
    #     for tag in tags:
    #         q = q.i

    def get_by_keyword(self, db: Session, *, keyword: str) -> List[Recipe]:
        return (
            db.query(Recipe)
            .filter(
                Recipe.__ts_vector__.op("@@")(
                    func.to_tsquery("english", f"{keyword}:*")
                )
            )
            .all()
        )

    def start_query(self, db: Session) -> Query:
        return db.query(Recipe)

    def with_keyword(self, q: Query, *, keyword: str) -> Query:
        return q.filter(
            Recipe.__ts_vector__.op("@@")(
                func.to_tsquery("english", f"{keyword.replace(' ', ' & ')}:*")
            )
        )

    def with_tags_and(self, q: Query, *, tags: List[str]) -> Query:
        for tag in tags:
            q = q.filter(Recipe.tags.any(Tag.name == tag))
        return q

    # TODO with_tags_or

    def sort_popularity(self, q: Query) -> Query:
        return q.order_by(Recipe.popularityScore.desc())

    def sort_views(self, q: Query) -> Query:
        return q.order_by(Recipe.totalViews.desc())

    def sort_best(self, q: Query) -> Query:
        return q.order_by(Recipe.rating.desc())

    # TODO move offset and limit before sort
    def execQuery(self, q: Query, *, skip: int, limit: int) -> List[Recipe]:
        return q.offset(skip).limit(limit).all()

    def get_all(self, db: Session):
        return db.query(Recipe).all()


recipe = CRUDRecipe(Recipe)
