from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.tag import TagCreate
from app.tests.utils.utils import random_lower_string


def test_create_tag(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    name = random_lower_string()
    data = {"name": name}
    r = client.post(
        f"{settings.API_V1_STR}/tags/",
        headers=superuser_token_headers,
        json=data,
    )
    assert 200 <= r.status_code < 300
    created_tag = r.json()
    tag = crud.tag.get_by_name(db, name=name)
    assert tag
    assert tag.name == created_tag["name"]


# TODO update tag test


def test_get_tags(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    r = client.get(
        f"{settings.API_V1_STR}/tags/",
        headers=superuser_token_headers,
    )

    assert 200 <= r.status_code < 300
    tags = r.json()
    assert tags
    assert len(tags) != 0


def test_delete_tags(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    name = random_lower_string()
    tag_in = TagCreate(name=name)
    tag = crud.tag.create(db, obj_in=tag_in)
    tag_id = tag.id

    r = client.delete(
        f"{settings.API_V1_STR}/tags/{tag_id}",
        headers=superuser_token_headers,
    )

    assert 200 <= r.status_code < 300
    assert r
    tag = crud.tag.get_by_id(db, id=tag_id)
    assert not tag
