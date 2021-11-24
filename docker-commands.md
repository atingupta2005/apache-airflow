docker system prune -a

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker system prune -a

docker system prune --volumes

docker network prune

docker volume prune
