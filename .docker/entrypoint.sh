#!/bin/bash

set -e

# Wait for the database to be available.
while ! nc -z ${DB_HOST} ${DB_PORT}; do sleep 1; done

# Start the server
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
