FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN apt-get update
RUN apt-get install python3 python3-pip libpq-dev python-dev -y 

RUN mkdir -p /airflow

ENV AIRFLOW_HOME /airflow
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN postgresql+psycopg2://db/airflow
ENV AIRFLOW__CORE__EXECUTOR LocalExecutor
ENV AIRFLOW__CORE__DAGS_FOLDER /code/dags
ENV AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION True
ENV AIRFLOW_CONN_POSTGRES_DJANGO postgresql://root@db/django

RUN pip3 install -r requirements.txt
RUN pip3 install apache-airflow[postgres]

ENV DJANGO_SETTINGS_MODULE=dit.settings.docker

RUN chmod +x /code/airflow_entrypoint.sh

ENTRYPOINT [ "/code/airflow_entrypoint.sh" ]
