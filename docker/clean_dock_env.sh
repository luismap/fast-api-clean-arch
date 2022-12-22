#remove container postgresql container
docker ps -a | grep postgres-apidev | awk '{print $1}' | xargs docker container rm

#remove volume
docker volume rm docker_local_pgdata

#remove container for pgadmin
docker ps -a | grep pgadmin-apidev | awk '{print $1}' | xargs docker container rm

#remove volume for pgadmin
docker volume rm  docker_pgadmin-data

#remove container for sqllite
docker ps -a | grep sqlite3 | awk '{print $1}' | xargs docker container rm

#remove volume for sqllite
docker volume rm  docker_sql_lite