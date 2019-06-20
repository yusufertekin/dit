FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN apt-get update
RUN apt-get install libpq-dev python-dev -y

RUN pip3 install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=dit.settings.docker

ENTRYPOINT [ "/code/web_entrypoint.sh" ]
