#!/bin/sh

python3 wait_for_it.py
echo =Initializing DB=
airflow initdb
echo =Starting scheduler=
airflow scheduler &
echo =Sleeping for 10 seconds=
sleep 10
echo Unpausing dit
airflow unpause dit
echo Starting airflow webserver
airflow webserver -p 8080 
