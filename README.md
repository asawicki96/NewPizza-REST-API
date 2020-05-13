# NewPizza

An **REST API** application, designed by means of **django-REST framework**, to provide backend support for restaurant websites.
It allows to create, update & etc.. db objects such as Food, Addition, Order. ListViews allows to search and filter object wchich
is realised by means of **ElasticSearch** and **taggit**.
Authentication and registration views are also provided. Authenticated User can create Orders and update
his account. Admin user can create and update food and addition objects. Application is provided with default django admin site
but it has endpoints to CRUD operations also. 

Steps to run application:
- get the repo,
- install ElasticSearch 7.6.2, 
- create virtualenv and install dependencies mentioned in Pipfile & Pipfile.lock,
- run python manage.py makemigrations, manage.py migrate,
- run python manage.py createsuperuser ...,
- run ElasticSearch,
- run python manage.py runserver,

List of endpoints:

- api/schema/ : API schema,
- admin/ : default admin views,
- api/food/ : by HTTP GET method -> food list paginated by 20
             *if searchfield parameter provided returns searched results
              allows search by: name, slug, description, ingredients
             * if tags parameter provided returns filtered by tags results,
             
- api/food/<int:pk>/ : by HTTP GET method -> food detail view
- api/food/ : by HTTP POST method -> food creation view (only for authenticated staff user)
- api/food/ : by HTTP PUT method -> food update view (only for authenticated staff user)

- api/additions/ : by HTTP GET method -> additions list paginated by 20
                  *if searchfield parameter provided returns searched results
                   allows searching by: name, slug, description
                  *if tags parameter provided returns filtered by tags results,
- api/additions/<int:pk>/ : by HTTP GET method -> additions detail view,
- api/additions/ : by HTTP POST method -> additions creation view (only for authenticated staff user),
- api/additions/ : by HTTP PUT method -> additions update view (only for authenticated staff user),

- api/user/create : by HTTP POST method -> user creation view,
- api/user/update/<pk> : by HTTP PUT method -> user update view,
- api/user/login/ : by HTTP POST method -> user login view,
- api/user/logout/ : by HTTP GET method -> user logout view (deleting user's session data).

