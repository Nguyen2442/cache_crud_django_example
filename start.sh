#!/bin/bash


mkdir -p /tmp/src


echo "Activating the virtualenv environment"
. ./src-env/bin/activate


echo "Install the required packages"
pipenv install --dev

echo "run the migrations files"
python3 manage.py migrate

echo "Starting the service up using dev server"
python3 manage.py runserver 0.0.0.0:8000