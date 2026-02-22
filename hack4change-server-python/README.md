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
From a pipenv shell:

- `pytest` will run all tests.
- `pytest <name>` will run tests in the named file or directory. For example, `pytest test_main.py` will run any tests in the `test_main.py` file.

### Running/Building
In order to run a production version of the server, you can use `python main.py`.

## Reference Material
You can learn more about FastAPI by referencing the documentation at https://fastapi.tiangolo.com/learn/.