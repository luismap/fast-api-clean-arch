#remove container postgresql container
docker ps -a | grep postgres-apidev | awk '{print $1}' | xargs docker container rm

#remove volume
docker volume rm docker_local_pgdata