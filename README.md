Todo
---------
- [ ] testcode
- [ ] docker network

Quickstart
----------

First, run ``PostgreSQL``, set environment variables and create database. For example using ``docker``: ::

    export POSTGRES_DB=postgres POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres
    docker run --name pgdb --rm -e POSTGRES_USER="$POSTGRES_USER" -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" -e POSTGRES_DB="$POSTGRES_DB" postgres
    export POSTGRES_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgdb)
    createdb --host=$POSTGRES_HOST --port=$POSTGRES_PORT --username=$POSTGRES_USER $POSTGRES_DB

Then run the following commands to bootstrap your environment with ``poetry``: ::

    git clone https://github.com/ritter4u/fastapi-example-app
    cd fastapi-example-app
    poetry install
    poetry shell

Then create ``.env`` file (or rename and modify ``.env.example``) in project root and set environment variables for application: ::

    touch .env
    echo APP_ENV=dev >> .env
    echo DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
    echo SECRET_KEY=$(openssl rand -hex 32) >> .env
    echo POSTGRES_USER=$POSTGRES_USER >> .env
    echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env
    echo POSTGRES_HOST=$POSTGRES_HOST >> .env
    echo POSTGRES_PORT=$POSTGRES_PORT >> .env
    echo POSTGRES_DB=$POSTGRES_DB >> .env

To run the web application in debug use::

    alembic upgrade head
    uvicorn app.main:app --reload

If you run into the following error in your docker container:

   sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: No such file or directory
   Is the server running locally and accepting
   connections on Unix domain socket "/tmp/.s.PGSQL.5432"?

Ensure the DATABASE_URL variable is set correctly in the `.env` file.
It is most likely caused by POSTGRES_HOST not pointing to its localhost.

   DATABASE_URL=postgresql://postgres:postgres@0.0.0.0:5432/postgres

Deployment with Docker
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
First, create ``.env`` file like in `Quickstart` section or modify ``.env.example``.
``POSTGRES_HOST`` must be specified as `db` or modified in ``docker-compose.yml`` also.
Then just run::

    docker compose up -d 

Application will be available on ``localhost`` in your browser.

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
