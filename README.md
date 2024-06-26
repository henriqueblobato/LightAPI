
[![Upload Python Package](https://github.com/henriqueblobato/LightAPI/actions/workflows/python-publish.yml/badge.svg)](https://github.com/henriqueblobato/LightAPI/actions/workflows/python-publish.yml)

# LightAPI

## Overview
LightAPI is a lightweight framework designed for quickly building API endpoints using Python's native libraries. It aims to simplify API development by providing a simple and easy-to-use interface while maintaining flexibility and performance.

## Features
- **Simplicity**: LightAPI allows developers to define API endpoints with minimal boilerplate code, making it easy to get started with API development.
- **Flexibility**: Developers can define models using SQLAlchemy's ORM and create API endpoints for CRUD operations with just a few lines of code.
- **Performance**: LightAPI leverages asynchronous programming with aiohttp to handle concurrent requests efficiently, ensuring high performance for your API.

## How it Works
LightAPI uses the following components to create API endpoints:
- **SQLAlchemy**: For defining database models and interacting with the database.
- **aiohttp**: For handling async HTTP requests and routing.

## Using LightAPI
To use LightAPI in your project, simply import the `LightApi` class and create an instance of it. Then, register your database models and start the API server. Here's a basic example:

```python
from sqlalchemy import Column, Integer, String
from database import CustomBase
from lightapi import LightApi


class Person(CustomBase):
    pk = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    email = Column(String, unique=True)


if __name__ == '__main__':

    app = LightApi()
    app.register({'/person': Person})
    app.run()
```

In summary, this code sets up a basic RESTful API using the LightApi framework, defines a single SQLAlchemy model (`Person`), and associates it with the `/person` endpoint for performing CRUD operations on the `Person` table in the database.

This will create all RESTful endpoints for the `Person` model, allowing you to perform CRUD operations on the `person` table in your database.

| Method   | Endpoint           | Description                                          |
|----------|--------------------|------------------------------------------------------|
| GET      | /person            | Retrieve all records from the `person` table.        |
| GET      | /person/{pk}       | Retrieve a specific record by primary key.           |
| POST     | /person            | Create a new record in the `person` table.           |
| PUT      | /person/{pk}       | Update an existing record by primary key.            |
| DELETE   | /person/{pk}       | Delete a record by primary key.                      |
| PATCH    | /person/{pk}       | Partially update a record by primary key.            |
| OPTIONS  | /person            | Retrieve information about the `person` endpoint.    |
| HEAD     | /person            | Retrieve the headers for the `person` endpoint.      |

## Databases compatibility
LightAPI is compatible with the following databases:

- **SQLite**: A self-contained, serverless, zero-configuration SQL database engine.
- **PostgreSQL**: An advanced open-source SQL database system known for its robustness and features.
- **MySQL & MariaDB**: Both MySQL and MariaDB are popular open-source relational database management systems, and SQLAlchemy supports them interchangeably due to their similarity.
- **Oracle**: A powerful commercial relational database management system widely used in enterprise environments.
- **MS-SQL**: Microsoft SQL Server, a relational database management system developed by Microsoft.

LightAPI uses SQLAlchemy as an ORM to interact with these databases, providing a consistent interface for defining models and performing CRUD operations across different database systems.

## Connecting to DB
To connect to a database, you need to provide the database URL in the `DATABASE_URL` environment variable. LightAPI will automatically connect to the database using the URL provided.
```python
os.environ['DATABASE_URL'] = "postgresql://user:password@postgresserver/db"

if __name__ == '__main__':
    app = LightApi()
    app.register({'/person': Person})
    app.run()
```
If no `DATABASE_URL` is provided, LightAPI will default to using an in-memory SQLite database for local development.

## Why LightAPI?
LightAPI is designed to streamline the process of building API endpoints, allowing developers to focus on defining their models and business logic without getting bogged down in the details of request handling and routing. With its simple and intuitive interface, LightAPI enables faster API development, making it ideal for prototyping, small projects, or situations where speed is of the essence.

## Installation
You can install LightAPI using pip:

```bash
pip install LightApi
```
**Pypi page**: https://pypi.org/project/LightApi/

## Contributing
If you'd like to contribute to LightAPI, please fork the repository and submit a pull request. You can also open an issue if you encounter any bugs or have suggestions for new features.

The LightAPI project is in its nascent stage, aimed at providing a minimalist yet efficient framework for swiftly developing API endpoints. While it offers a basic set of functionalities to streamline the process of building RESTful APIs, it remains open to enhancements and contributions from the community. We welcome and encourage developers to contribute to the project, but with a core principle in mind: keeping the API minimal and straightforward. By adhering to simplicity, we ensure that LightAPI remains accessible and easy to use, catering to a wide range of use cases without unnecessary complexity. Contributions that align with this philosophy, focusing on improving performance, adding essential features, or refining existing functionality, are highly appreciated. Together, let's build a robust yet uncomplicated tool for API development.

## License
LightAPI is released under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For any questions, feedback, or suggestions, feel free to reach out to the project maintainer,
Henrique Lobato at email `iklobato1@gmail.com`
