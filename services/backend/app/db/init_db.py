from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base
from app.db.base import Base

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=db.get_bind())

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)

    # Add tags and products -> TODO move to seperate file
    initialTags = [
        'Pasta',
        'Tomatoes',
        'Mushrooms',
        'Soups',
        'In oven',
        'Chinese cuisine',
        'Italian cuisine',
        'Polish cuisine',
        'Vege',
        'Gluten Free',
        'Fast',
        'Onion',
        'Cheese' 
    ]
    for tag in initialTags:
        db_tag = crud.tag.get_by_name(db=db, name=tag)
        if not db_tag:
            tag_in = schemas.TagCreate(name=tag)
            crud.tag.create(db=db, obj_in=tag_in)

    initialProducts = [
        'pasta',
        'onion',
        'pepper',
        'tomatoes',
        'garlic',
        'olive oil',
        'water',
        'meat',
        'seasoning',
        'salt',
        'black pepper',
        'mozarella',
    ]
    for product in initialProducts:
        db_product = crud.product.get_by_name(db=db, name=product)
        if not db_product:
            product_in = schemas.ProductCreate(name=product, price=1)
            crud.product.create(db=db, obj_in=product_in)
    
