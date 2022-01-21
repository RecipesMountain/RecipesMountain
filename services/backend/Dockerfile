FROM python:3.10-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

FROM base as builder

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.12

RUN pip install "poetry==$POETRY_VERSION" \
    && python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate && poetry install --no-interaction --no-dev --no-root

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM builder as test

RUN . /venv/bin/activate && poetry install --no-interaction --no-root

FROM base as final

RUN groupadd -r user && useradd -r -s /bin/false -g user user
COPY --chown=user:user alembic.ini docker-entrypoint.sh ./
COPY --chown=user:user alembic ./alembic
COPY --from=builder --chown=user:user /venv /venv
ENV PATH=/venv/bin:$PATH
EXPOSE 5000
USER user

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
