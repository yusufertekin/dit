#!/bin/sh

python3 wait_for_it.py
echo Migrating
python3 manage.py migrate
echo Running the local server
python3 manage.py runserver 0.0.0.0:8000
