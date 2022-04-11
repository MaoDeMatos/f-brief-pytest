# Pytest initiation

Studying project about softare automated tests and Continuous Integration.

## Prerequisites

Python 3.10 need to be installed on your host.

```sh
pip install pipenv
pipenv install
```

## Run

To start the app:

```sh
pipenv run flask run
```

## Tests

`pytest` arguments :

- `-v` verbose
- `-s` activates `print()`
- `--collect-only` do not run tests, simply read the files

```sh
pipenv run pytest -s
```
