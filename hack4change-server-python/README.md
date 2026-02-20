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

This will run a server that reloads on file change, if you do not specify the address and port it will run on port 8000 instead

`python manage.py runserver 0.0.0.0:8081`

### Tests

For Unit tests:

`python manage.py test`

For E2E/API tests, make sure your dev server is running on port 8081 and:

`pytest e2e/test_api.py`

### Running/Building

You can use the same command as the dev server, but go into the `settings.py` file and change the key, debug flags, etc... 

`Django` has documentation on running it other ways as well if desired.

## Reference Material

See https://docs.djangoproject.com/en/6.0/ for more information on Django patterns along with tutorials.
