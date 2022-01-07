from typing import Tuple
from uuid import UUID
import uuid
from fastapi.testclient import TestClient
from app.core.config import settings
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app.schemas.recipe import RecipeCreate
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_lower_string, random_email
from app.tests.utils.recpies import createRecpies, createRecpiesWithTags


def test_search(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    title = random_lower_string()
    createRecpies(db, title, 2)
    r = client.get(
        f"{settings.API_V1_STR}/recipes/search?keywords={title}&skip=0&limit=100&sort=popular&tagsConnect=and",
        headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    recpies = r.json()
    print(recpies)
    assert len(recpies) >= 2
    for recpie in recpies:
        assert title in recpie["title"]


def test_bad_tags_connect(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    title = random_lower_string()
    createRecpies(db, title, 2)
    r = client.get(
        f"{settings.API_V1_STR}/recipes/search?keywords={title}&skip=0&limit=100&sort=popular&tagsConnect=xx",
        headers=superuser_token_headers,
    )
    assert r.status_code == 400
    detail = r.json()
    assert detail["detail"] == "Bad tags connect"


def test_bad_sort(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    title = random_lower_string()
    createRecpies(db, title, 2)
    r = client.get(
        f"{settings.API_V1_STR}/recipes/search?keywords={title}&skip=0&limit=100&sort=popularrrr&tagsConnect=and",
        headers=superuser_token_headers,
    )

    assert r.status_code == 400
    detail = r.json()
    assert detail["detail"] == 'Bad sort, aviable "popular", "views", "best", "nosort"'


def test_search_tags(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    title = random_lower_string()
    tagsNames = [random_lower_string(), random_lower_string()]
    createRecpiesWithTags(db, title, 10, tagsNames)

    r = client.get(
        f"{settings.API_V1_STR}/recipes/search?tags={tagsNames[0]}&tags={tagsNames[1]}&skip=0&limit=10&sort=popular&tagsConnect=and",
        headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    recpies = r.json()
    print(recpies)
    assert len(recpies) == 10
    for recpie in recpies:
        assert title in recpie["title"]
