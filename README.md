<h1> Development of a financial manager (test task) for Akvelon </h1>
<h3> v.0.1 </h3>


<h2> Swagger on host: </h2> 
https://test.sigalgleb.ru/swagger/

<h2> Run project </h2> 

The project is packaged in docker, which includes:
- Automatic database creation;
- Migrations;
- Some tests;


```
docker-compose up --build
```

<h2> Technology stack: </h2> 

- Python;
- Django;
- Django Rest Framework;
- Swagger;
- Docker;
- PostgreSQL;
- Nginx;
- Gunicorn;

<h2> TODO: </h2> 

1. General: Replace current access with the authorization system;
2. Tests: Add more tests;
3. Swagger: Make function for dynamic fields creation;
4. Swagger: Find some way to replace field's type and description;
