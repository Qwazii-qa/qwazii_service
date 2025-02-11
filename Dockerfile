FROM python:3.13-slim-bookworm

RUN apt-get update && \
    apt-get install python3-dev default-libmysqlclient-dev build-essential -y

RUN mkdir qwazii_service
WORKDIR /qwazii_service

RUN pip install --upgrade pip
RUN pip install poetry


# install packages via poetry
COPY poetry.lock /qwazii_service/poetry.lock
COPY pyproject.toml /qwazii_service/pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root


ADD . /qwazii_service

CMD [ "sh", "docker-entrypoint.sh" ]
