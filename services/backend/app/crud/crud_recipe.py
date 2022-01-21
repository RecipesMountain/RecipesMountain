from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.functions import func

from app.crud.base import CRUDBase
from app import crud
from app.models.recipe import Recipe
from app.models.tag import Tag
from app.models.product import Product

from app.models.stage import Stage

from app.models.recipe_tags import RecipeTags
from app.models.products_in_stages import ProductsInStages
from app.models.favorite_recipes import FavoriteRecipes

from app.schemas.recipe import RecipeCreate, RecipeUpdate
from app.models.recipe_ratings import RecipeRatings


from uuid import UUID


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    def get_by_tags_and(self, db: Session, *, tags: List[Recipe]) -> List[Recipe]:
        q = db.query(Recipe)
        for tag in tags:
            q = q.filter(Recipe.tags.any(tag.name.contains(tag)))
        return q.all()

    def get_by_keyword(self, db: Session, *, keyword: str) -> List[Recipe]:
        return (
            db.query(Recipe)
            .filter(
                Recipe.__ts_vector__.op("@@")(
                    func.to_tsquery("english", f"{keyword.replace(' ', ' & ')}:*")
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

    def get_favorite_recepies(self, db: Session, *, user_id: UUID) -> List[Recipe]:
        return (
            db.query(Recipe)
            .filter(Recipe.users_favorite.any(FavoriteRecipes.user_id == user_id))
            .all()
        )

    def add_of_delete_from_favorites(
        self, db: Session, *, user_id: UUID, recipe_id: UUID
    ):
        liked_recipe = (
            db.query(FavoriteRecipes)
            .filter(
                FavoriteRecipes.recipe_id == recipe_id,
                FavoriteRecipes.user_id == user_id,
            )
            .first()
        )
        if liked_recipe:
            db.delete(liked_recipe)
            db.commit()
            return False
        else:
            liked_recipe = FavoriteRecipes(user_id=user_id, recipe_id=recipe_id)
            db.add(liked_recipe)
            db.commit()
            db.refresh(liked_recipe)
            return True

    def is_liked(self, db: Session, *, user_id: UUID, recipe_id: UUID):
        liked_recipe = (
            db.query(FavoriteRecipes)
            .filter(
                FavoriteRecipes.recipe_id == recipe_id,
                FavoriteRecipes.user_id == user_id,
            )
            .first()
        )
        if liked_recipe:
            return True
        else:
            return False

    def create(self, db: Session, *, obj_in: RecipeCreate, owner_id: UUID) -> Recipe:

        db_obj = Recipe(
            title=obj_in.title,
            cookingTime=obj_in.cookingTime,
            difficulty=obj_in.difficulty,
            calories=obj_in.calories,
            portion=obj_in.portion,
            rating=obj_in.rating,
            owner_id=owner_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        for stage in obj_in.stages:
            db_stage_obj = Stage(name=stage.name, content=stage.content, recipe=db_obj)
            db.add(db_stage_obj)
            db.commit()
            db.refresh(db_stage_obj)

            for product in stage.products:
                # this should be in crud products
                prod = db.query(Product).filter(Product.name == product.name).first()
                prod_id = 0
                if not prod:
                    db_obj_prod = Product(name=product.name, price=0)
                    db.add(db_obj_prod)
                    db.commit()
                    db.refresh(db_obj_prod)
                    prod_id = db_obj_prod.id
                else:
                    prod_id = prod.id

                db_product_stage_obj = ProductsInStages(
                    product_id=prod_id,
                    stage_id=db_stage_obj.id,
                    amount=product.amount,
                    amount_unit=product.amount_unit,
                )
                db.add(db_product_stage_obj)
                db.commit()
                db.refresh(db_product_stage_obj)

        for tag in obj_in.tags:
            db_tag_recipe_obj = RecipeTags(recipe_id=db_obj.id, tag_id=tag.id)
            db.add(db_tag_recipe_obj)
            db.commit()
            db.refresh(db_tag_recipe_obj)
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, obj_in: RecipeUpdate, recipe_id: UUID) -> Recipe:
        recipe_old = db.query(Recipe).filter(Recipe.id == recipe_id).first()

        for key, value in obj_in:
            if value is not None:
                # Updating basic parameters
                if value is not None and key not in [
                    "tags",
                    "stages",
                    "totalViews",
                    "rating",
                ]:
                    setattr(recipe_old, key, value)
                    db.commit()

                # Updating tags
                if key == "tags":
                    recipe_tags = db.query(RecipeTags).filter(
                        RecipeTags.recipe_id == recipe_id
                    )
                    for tag in recipe_tags:
                        db.delete(tag)
                        db.commit()
                    for tag in obj_in.tags:
                        db_tag_recipe_obj = RecipeTags(
                            recipe_id=recipe_id, tag_id=tag.id
                        )
                        db.add(db_tag_recipe_obj)
                        db.commit()
                        db.refresh(db_tag_recipe_obj)

                # Updating stages
                if key == "stages":

                    recipe_stages = db.query(Stage).filter(Stage.recipe_id == recipe_id)
                    for stage in recipe_stages:

                        for product in stage.products:
                            db.delete(product)
                            db.commit()
                        db.delete(stage)
                        db.commit()
                    for stage in obj_in.stages:
                        db_stage_obj = Stage(
                            name=stage.name, content=stage.content, recipe=recipe_old
                        )
                        db.add(db_stage_obj)
                        db.commit()
                        db.refresh(db_stage_obj)

                        if stage.products:
                            for product in stage.products:
                                # this should be in crud products
                                prod = (
                                    db.query(Product)
                                    .filter(Product.name == product.name)
                                    .first()
                                )
                                prod_id = 0
                                if not prod:
                                    db_obj_prod = Product(name=product.name, price=0)
                                    db.add(db_obj_prod)
                                    db.commit()
                                    db.refresh(db_obj_prod)
                                    prod_id = db_obj_prod.id
                                else:
                                    prod_id = prod.id

                                db_product_stage_obj = ProductsInStages(
                                    product_id=prod_id,
                                    stage_id=db_stage_obj.id,
                                    amount=product.amount,
                                    amount_unit=product.amount_unit,
                                )
                                db.add(db_product_stage_obj)
                                db.commit()
        return recipe_old

    def get_by_id(self, db: Session, *, recipe_id: UUID) -> Recipe:
        return db.query(Recipe).filter(Recipe.id == recipe_id).first()

    def add_image(self, db: Session, *, recipe_id: UUID, file: bytes):
        recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
        recipe.image_blob = file
        db.add(recipe)
        db.commit()
        db.refresh(recipe)
        return recipe

    def get_and_incrementViews(self, db: Session, *, recipe_id: UUID) -> Recipe:
        recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if not recipe:
            return None
        recipe.totalViews += 1
        recipe.popularityScore += 1
        db.add(recipe)
        db.commit()
        db.refresh(recipe)
        return recipe

    def rate(
        self, db: Session, *, recipe_id: UUID, user_id: UUID, newRating: int
    ) -> int:
        rating = (
            db.query(RecipeRatings)
            .filter(
                RecipeRatings.recipe_id == recipe_id, RecipeRatings.user_id == user_id
            )
            .first()
        )
        if rating:
            rating.rating = newRating
        else:
            rating = RecipeRatings(
                recipe_id=recipe_id, user_id=user_id, rating=newRating
            )
        print(rating)
        db.add(rating)
        db.commit()
        db.refresh(rating)

        ratingUpdate = (
            db.query(func.avg(RecipeRatings.rating).label("average"))
            .filter(RecipeRatings.recipe_id == recipe_id)
            .scalar_subquery()
        )
        print(ratingUpdate)
        recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

        recipe.rating = ratingUpdate

        print(recipe.rating)

        db.add(recipe)
        db.commit()
        db.refresh(recipe)

        return recipe.rating

    def make_products_names_string(self, db: Session, obj_in: Recipe) -> str:
        query = ""

        for stage in obj_in.stages:
            for product in stage.products:
                query = (
                    query
                    + " "
                    + str(int(product.amount))
                    + " "
                    + product.amount_unit
                    + " "
                    + product.name
                    + " and"
                )

        return query


recipe = CRUDRecipe(Recipe)
