from typing import Tuple
from uuid import UUID, uuid4
from app.models.comment import Comment
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app.schemas import CommentCreate, CommentUpdate
from app.tests.utils.utils import random_lower_string
from app.tests.utils.user import create_random_user
from app.tests.utils.recpies import createRecpie
from app.models.user import User


def test_comment_create(db: Session) -> None:
    content = random_lower_string()
    comment, _, _ = createComment(db, content)
    assert comment.content == content


def test_comment_get(db: Session) -> None:
    content = random_lower_string()
    comment, _, recipe_id = createComment(db, content)
    comment = crud.comment.get(db, recipe_id=recipe_id)[0]
    assert comment.content == content


def test_comment_delete(db: Session) -> None:
    content = random_lower_string()
    comment, _, recipe_id = createComment(db, content)
    assert crud.comment.delete(db, comment_id=comment.id)
    comments = crud.comment.get(db, recipe_id=recipe_id)
    assert len(comments) == 0


def createComment(db: Session, content: str) -> Tuple[Comment, User, UUID]:
    fakerecpie, nameRecpie = createRecpie(db)
    fakeowner = create_random_user(db)
    content_in = CommentCreate(content=content)
    comment = crud.comment.create(
        db, obj_in=content_in, owner_id=fakeowner.id, recipe_id=fakerecpie
    )
    return comment, fakeowner, fakerecpie
