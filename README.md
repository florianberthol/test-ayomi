1 - Installation 
=================
Initialiser et démarrer docker
```
docker compose up -d
```
Initialiser la base de données 
````
docker exec -i mysql-db mysql -h db -u fastapi_user --password=fastapi_password < db/db.sql
````
2- Test
========
 - Les calcules
```
curl -d '{"operation": "4 2 + 2 * 10 5 - 2 / +"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/calcule
```
 - Recuperer le dump
```
curl http://127.0.0.1:8000/dump > dump.csv 
```