# noteCreation-Flask-JWT-API
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
<br>

## Description

A simple web application API that allows a registered user to create and download Notes.

## Pre - requisites

* Docker & docker-compose

## Instalation

Once you clone this repository, you must do the following steps:

### .env.example file

In order for this example to work, you must rename the `.env.example` to `.env` with the following command:
```
mv .env.example .env
```

### Build the docker image

Build docker image using the following command:

```
 docker-compose up --build --remove-orphans
 ```
 That should do it.

 ### Documentation and Use

 You can check the endpoints available in swagger by visiting the following URL in a browser:

 ```
    http://localhost:5000/api/v1/swagger/
 ```

You can use POSTMan for testing.

 