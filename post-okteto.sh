#!/bin/sh

echo "starting app..."
echo " "
cd /app

touch /app/requirements.txt && pip install --trusted-host pypi.python.org -r /app/requirements.txt

python main.py
