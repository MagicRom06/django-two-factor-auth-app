FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-two-factor-auth-app/

COPY Pipfile Pipfile.lock /django-two-factor-auth-app/
RUN pip install pipenv && pipenv install --system

COPY . /django-two-factor-auth-app/