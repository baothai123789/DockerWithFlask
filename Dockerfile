FROM python:3.12-slim-bookworm
ARG ENV
ENV MYENV=${ENV}\
    DEV_DATABASE_NAME=../resource/instances/bookshopapp.sqlite\
    PROD_DATABASE_URI=mysql+pymysql://root:22042004bao@myappdb:3306/bookshopapp\
    GUNICORN_PROCESSES=3\
    GUNICORN_THREADS=3\
    GUNICORN_BIND=0.0.0.0:8080 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.7.1


WORKDIR /app
COPY poetry.lock pyproject.toml  /app/
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install coincurve 
RUN pip install poetry
RUN poetry install --no-interaction
COPY . /app/
EXPOSE 8080
CMD ["./docker-entrypoint.sh"]



