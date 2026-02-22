# Python-Django Sample Application

A sample web server in Python.

## Requirements
- `python 3+`
- `pipenv`

## Setup Process

- Enter the root directory and run `pipenv install` to fetch all the dependencies.
- Then enter `pipenv shell` and you will be in a shell with everything setup and ready to go.
- If you need to add dependencies as you go use `pipenv install <dep>` from the root directory so it's added to the `/Pipfile`. You may need to exit and re-enter your `pipenv shell` to do so.

## Commands

### Dev Server

This will run a server that rebuilds and reloads on file change, if you do not specify the address and port it will run on port 8000 instead

`fastapi dev main.py --port 8080`

### Tests

For Unit tests:

`python manage.py test`

For E2E/API tests, make sure your dev server is running on port 8081 and:

`pytest e2e/test_api.py`

### Running/Building

In order to build and run the application, you can use `python main.py`.

## Reference Material

TODO FastAPI