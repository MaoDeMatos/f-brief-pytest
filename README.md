# Pytest initiation

Main repo & CI at [github.com/MaoDeMatos/f-brief-pytest](https://github.com/MaoDeMatos/f-brief-pytest).

Studying project about softare automated tests and Continuous Integration.

## Prerequisites

Python 3.10 OR Docker needs to be installed on your host.

To use with Python, you'll need pipenv.

```sh
# Install pipenv
pip install pipenv
# Install dependencies
pipenv install
```

Run the container with `docker-compose up -d --build`

## Flask app

To start the app (only displays "Hello world") :

```sh
pipenv run flask run
```

## Tests

To run tests in Docker, simply execute the commands in an interactive shell.

`pytest` arguments :

- `-v` verbose
- `-s` enables stdout response (eg: `print()`)
- `-m` search by marker
- `-k` search by regex (in function name)
- `--collect-only` do not run tests, simply read the files

You can find custom markers used in [`pytest.ini`](./pytest.ini).

Use this to run all tests and generate and HTML report (located [here](./__tests__/report.html)) :

```sh
pipenv run test -v -s
```

If you use `--collect-only` with this, you'll generate a blank report.

Use `pytest` if you don't want to generate a report :

```sh
pipenv run pytest -v -s
```
