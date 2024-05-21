# REST API Design Patterns

## REST Resource Naming Conventions
1. Use nouns for resource names
    - `/products`
    - `/orders`
    - `/customers`
2. Use plural nouns for collection names
    - `/products`
    - `/orders`
    - `/customers`
3. Not using singular nouns for resource names
    - `/products/{id}`
    - `/orders/{id}`
    - `/customers/{id}`
4. Use hyphens to separate words
    - `/product-categories`
    - `/product-reviews`
5. Use lowercase letters
    - `/products`
    - `/orders`
    - `/customers`
6. Use query params for filtering, sorting, and pagination
    - `/products?category=electronics`
    - `/products?sort=price`
    - `/products?limit=10&offset=20`


## Factory Application Pattern
The Factory Application Pattern is a design pattern used to create instances of objects without specifying the exact class of the object that will be created. In the context of Flask, the Factory Application Pattern is commonly used to create different instances of the application based on configuration.

## Set Up
- Create and activate virtual environment
    - Windows: `python -m venv venv && venv\Scripts\activate`
    - Mac/Linux: `python3 -m venv venv && . venv/bin/activate`

- Project Structure:
```python
├── app.py
├── config.py
├── database.py
├── controllers
│   ├── __init__.py
├── models
│   ├── __init__.py
├── schemas
│   ├── __init__.py
├── requirements.txt
├── routes
│   ├── __init__.py
└── services
    ├── __init__.py
```
- Installs
``` bash
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy mysql-connector-python
```


### Models

The `models` folder contains the database models for the application, defined as classes that inherit from `db.Model`. Each model class represents a table in the database, with class attributes mapping to the table columns. These models are used to interact with the database, performing operations like creating, reading, updating, and deleting records. 

By defining your database schema in this way, you can easily manage and query your data using SQLAlchemy's ORM capabilities.


### Schemas

The `schemas` folder contains serialization and deserialization schemas for the application, created using Flask-Marshmallow. These schemas define the structure of the data exchanged between the application and clients, typically in JSON format.

Using schemas allows for easy validation and transformation of incoming and outgoing data, ensuring that it conforms to the expected format before being processed by the application. This helps in maintaining data integrity and handling errors gracefully.

Each schema class within this folder represents a specific data structure, mapping its fields to the corresponding attributes of the associated model classes. Flask-Marshmallow provides powerful features for defining these schemas, including validation, data formatting, and nested schema support.

By separating concerns and defining clear data contracts, schemas facilitate the development of robust and maintainable APIs in Flask applications.

### Controllers

The `controllers` folder contains the controller logic for the application, where the view functions are defined and connected to routes. These view functions handle incoming HTTP requests, interact with the database through models, and use schemas for data serialization and deserialization.

Controllers serve as the bridge between the client and the application, implementing the business logic and orchestrating the flow of data. They parse incoming requests, validate data, invoke appropriate model methods for database operations, and return responses to the client in the desired format.

By organizing the application logic into controllers, you can maintain a clear separation of concerns and achieve better code organization and reusability. Each controller module typically corresponds to a specific resource or feature of the application, containing related view functions.

Flask's routing mechanism maps URL patterns to specific controller functions, allowing for a clean and intuitive API design. Additionally, Flask's flexibility enables easy integration of middleware, authentication, and error handling within the controller logic.

Overall, the controllers folder plays a crucial role in defining the behavior and endpoints of the Flask application, providing a structured and maintainable approach to building web APIs.

### Services

The `services` folder contains service modules that encapsulate business logic and interact with the database. These services abstract away the details of database operations and provide a clean interface for the controllers to interact with.

Each service module typically corresponds to a specific domain or resource in the application. These modules encapsulate related functionalities and provide methods for performing operations such as creating, reading, updating, and deleting data.

Within each service module, you can find functions or classes that implement the desired business logic. These functions/classes may utilize SQLAlchemy's session management and ORM capabilities to interact with the database.

For example, consider a `productService.py` module that handles operations related to products. This module may contain methods like `save`, `get`, `update`, and `delete`, each responsible for performing a specific action on product data.

Services promote code reusability, maintainability, and testability by abstracting away the details of database operations. They allow for better separation of concerns and facilitate the implementation of complex business logic in a structured and organized manner.

Overall, the services folder plays a crucial role in defining the business logic and data access layer of the Flask application, providing a clean and modular approach to handling application functionalities.


### Routes

The `routes` folder contains the routing logic for the application, where the endpoints and Blueprints are defined. In Flask, Blueprints are a way to organize related application components, such as routes, views, and templates, into modular and reusable units.

Each Blueprint within the routes folder represents a distinct set of functionalities or resources in the application. Blueprints allow for better code organization and scalability by separating concerns and promoting modular design.

Within each Blueprint, you can define multiple endpoints, each mapped to a specific URL pattern and associated view function. These endpoints serve as the entry points for client requests, defining the behavior and response of the application.

By encapsulating related routes and views within Blueprints, you can easily manage and extend the functionality of the application. Blueprints also facilitate collaboration among team members by providing clear boundaries and promoting code reuse.

Flask's Blueprint mechanism enables the creation of flexible and maintainable web applications, allowing for the efficient development of APIs and web services.

Overall, the routes folder plays a crucial role in defining the structure and behavior of the Flask application, providing a scalable and modular approach to routing and endpoint management.
