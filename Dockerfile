FROM python:3.10-slim AS builder

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1

# to run poetry directly as soon as it's installed
ENV PATH="$POETRY_HOME/bin:$PATH"

# install poetry
RUN apt-get update \
    && apt-get install -y curl gcc python3-dev musl-dev libpq-dev iputils-ping \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && chmod 755 ${POETRY_HOME}/bin/poetry
RUN pip3 install asyncpg
WORKDIR /app

# copy only pyproject.toml and poetry.lock file nothing else here
COPY poetry.lock pyproject.toml ./

# this will create the folder /app/.venv
RUN poetry install

# ---------------------------------------------------------------------

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# COPY . ./
COPY app ./app
COPY .env ./.env
COPY alembic.ini ./alembic.ini

# copy the venv folder from builder image
COPY --from=builder /app/.venv ./.venv

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
