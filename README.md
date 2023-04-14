# Flask-CRUD-Docker

Curls

1. GET all people : 
```md
curl --location --request GET 'http://localhost:80/people'
```


2. POST Person :
```md
curl --location --request POST 'http://localhost:80/person' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name" : "Ninad",
    "dob" : "21.03.1998"
}'
```

3. PUT Person
```md
curl --location --request PUT 'http://localhost:80/person/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name" : "Ninad Sharma",
    "dob" : "12.03.98"
}'
```

4. DELETE Person
```md
curl --location --request DELETE 'http://localhost:80/person/1' \
--data-raw ''
```
