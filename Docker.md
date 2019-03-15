DOCKER COMMAND
==============
```
dockerizing django project
navigate to project directory
create Dockerfile
create docker-compose.yml
docker build . --rm # removes intermediate images
docker-compose run web python /code/manage.py migrate --noinput
pattern is shown above now each django command should have
`docker-compose run web python /code/manage.py` mandatorily

docker build .
docker-compose run web python /code/manage.py migrate --noinput
docker-compose run web python /code/manage.py createsuperuser
docker-compose up -d --build
docker-compose down
docker system prune -a : remove all unused docker images, container 
docker stop <container_name>

docker-compose build
docker-compose up -d
docker network create --attachable project_network
$ docker rm -f 1f061139ba04
```
