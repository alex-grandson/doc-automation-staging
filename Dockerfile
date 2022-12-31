FROM python:3.9-alpine3.17 as app

ARG APP_ENV=dev

ENV APP_ENV=${APP_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.2.2

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /src

COPY pyproject.toml /src

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY backend/ /src/backend


# TEST

FROM app AS test

COPY --from=app /src /src

COPY tests/ /src/tests


# DOCS

FROM test AS docs

ARG RELEASE_VERSION=0.1.0
ARG REPO_URL

ENV RELEASE_VERSION=${RELEASE_VERSION}
ENV REPO_URL=${REPO_URL}

RUN apk add --update make

RUN pip install sphinx-rtd-theme docutils==0.19

COPY --from=app /src /src

WORKDIR /src/docs

COPY docs ./

COPY *.md ../

RUN sphinx-apidoc -o ./source ..

CMD ["make", "html"]
