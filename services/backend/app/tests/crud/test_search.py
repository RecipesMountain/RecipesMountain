from sqlalchemy.orm import Session

from app import crud
from app.tests.utils.utils import random_lower_string
from app.tests.utils.recpies import createRecpie, createRecpies, createRecpiesWithTags


def test_full_title_search(db: Session) -> None:
    id, title = createRecpie(db)

    recpieSearch = crud.recipe.get_by_keyword(db, keyword=title)
    assert len(recpieSearch) > 0
    recpieSearch = recpieSearch[0]
    assert recpieSearch.id == id


def test_partial_title_search(db: Session) -> None:
    id, title = createRecpie(db)

    recpieSearch = crud.recipe.get_by_keyword(db, keyword=title[: int(len(title) / 2)])
    assert len(recpieSearch) > 0
    recpieSearch = recpieSearch[0]
    assert recpieSearch.id == id


def test_creating_search_queries(db: Session) -> None:
    title = random_lower_string()
    createRecpies(db, title, 30)
    q = crud.recipe.start_query(db)
    q = crud.recipe.with_keyword(q, keyword=title)
    q = crud.recipe.sort_popularity(q)
    recpies = crud.recipe.execQuery(q, skip=0, limit=25)

    assert len(recpies) == 25
    for recpie in recpies:
        assert recpie.title == title


def test_search_with_tags(db: Session) -> None:
    title = random_lower_string()
    tagsNames = [
        random_lower_string(),
        random_lower_string(),
        random_lower_string(),
        random_lower_string(),
    ]
    createRecpiesWithTags(db, title, 10, tagsNames)
    q = crud.recipe.start_query(db)
    q = crud.recipe.with_tags_and(q, tags=tagsNames)
    q = crud.recipe.sort_popularity(q)
    recpies = crud.recipe.execQuery(q, skip=0, limit=10)
    assert len(recpies) == 10
    for recpie in recpies:
        assert recpie.title == title
