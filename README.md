# restful-api-example
### Restful-api backend example use Python3
## Overview
for study backend & Python3.

experience flask & sqlalchemy ORM

build using Python3-Flask

### it contains method
- select
  - GET /user/select
  - POST /user/select?name={name}
- insert
  - POST /user/insert?name={name}&age={age}
- update
  - POST /user/update?uid={uid}&name={name}&age={age}
- delete
  - POST /user/delete?uid={uid}

### Database table architecture
- id(INT, Primary Key)
- uid(VARCHAR, len : 32)
- name(VARCHAR, len : 20)
- age(INT, unsigned)
- timestamp(TIMESTAMP)

## Project Structure:
```
restful-api-example/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── user_controller.py
│   └── db.py
├── config.py
├── config.yaml
├── LICENSE.md
├── migrate.py
├── README.md
├── requirements.txt
└── run.py
```
## Python extensions used:
- PyMySQL
- PyYAML
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQLAlchemy
- Flask-Migrate
- Flask-Script
- flask-marshmallow
- marshmallow-sqlalchemy
- marshmallow-jsonapi
