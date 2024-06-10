#!/bin/bash
cd src/bookshopapp


while ! poetry run flask db upgrade
do
     echo "Retry Migrate db..."
     sleep 1
done
echo $MYENV
if [[ "$MYENV" == "dev" ]];
then
    poetry run flask run --host=0.0.0.0 --port=8080
else
    cd ..
    poetry run gunicorn --config wsgi.py index:app
fi
