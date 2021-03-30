FROM python:3.9-alpine AS base

RUN pip install pipenv
RUN apk update

RUN mkdir -p /src/backend
WORKDIR /src/backend

ENV WORKON_HOME=/src/venvs
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apk add --update --no-cache \
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libffi openssl libpq wkhtmltopdf

# ---

FROM base AS build

RUN apk add build-base git libffi-dev openssl-dev cargo

COPY requirements.txt Pipfile* /src/backend/
RUN cd /src/backend && pipenv install

# ---

FROM base

COPY --from=build /src/venvs /src/venvs

CMD ["pipenv", "run", "uwsgi", "-b 8192", "--http-timeout", "300", "--harakiri", "300", "--enable-threads", "--py-autoreload", "1", "--http", "0.0.0.0:5000", "--module", "wsgi", "--die-on-term", "--uid", "nobody"]
