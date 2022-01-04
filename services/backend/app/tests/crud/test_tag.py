from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app.schemas.tag import TagCreate, TagUpdate
from app.tests.utils.utils import random_lower_string


def test_create_tag(db: Session) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    assert tag.name == name


def test_update_tag(db: Session) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    newName = random_lower_string()
    tag_in = TagUpdate(name=newName, id=tag.id)
    tag = crud.tag.update(db, db_obj=tag, obj_in=tag_in)
    assert tag.name == newName


def test_create_tag_get(db: Session) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    assert tag.name == name
    tag = crud.tag.get_by_name(db, name=name)
    assert tag.name == name


def test_get_by_name(db: Session) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    tag = crud.tag.get_by_name(db, name=name)
    assert tag.name == name


def test_get_page(db: Session) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    tag = crud.tag.get_by_name(db, name=name)
    assert tag.name == name


def test_delete(db: Session) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    assert crud.tag.delete(db, id=tag.id)
    tag = crud.tag.get_by_name(db, name=name)
    assert tag == None


##TODO test update
