from fastapi import APIRouter

from app.api.endpoints import comments, login, products, recipes, tags, users

api_router = APIRouter()
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
