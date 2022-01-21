#!/bin/sh

if [ -z "$DISABLE_MIGRATIONS" ] || [ "$DISABLE_MIGRATIONS" != 1 ]; then
    alembic upgrade head
fi

exec "$@"
