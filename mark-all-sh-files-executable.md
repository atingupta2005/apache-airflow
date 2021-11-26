```
find ./ -name "*.sh" -exec chmod +x {} \;
```

- After that we need to delete the image and recreate it as the image has the shell script which doesn't execution rights
```
docker-compose -f docker-compose-LocalExecutor.yml down --rmi all
```
docker-compose -f --rmi all
