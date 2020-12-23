#!/bin/sh
docker build -t reliable .
docker-compose -f docker-compose.yml up -d
docker exec -it reliable_web_1 python3 /home/docker/code/manage.py collectstatic --noinput
#docker exec -it reliable_web_1 python3 /home/docker/code/manage.py migrate --noinput