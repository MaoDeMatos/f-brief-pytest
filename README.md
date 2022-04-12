# Pytest initiation

Studying project about softare automated tests and Continuous Integration.

## Prerequisites

Python 3.10 need to be installed on your host.

```sh
pip install pipenv
pipenv install
```

## Flask app

To start the app:

```sh
pipenv run flask run
```

## Tests

`pytest` arguments :

- `-v` verbose
- `-s` enables stdout response (eg: `print()`)
- `-m` search by marker
- `-k` search by regex (in function name)
- `--collect-only` do not run tests, simply read the files

You can find custom markers used in [`pytest.ini`](./pytest.ini)

Use this to run all tests and generate and HTML report :

```sh
pipenv run test -v -s
```

If you use `--collect-only` with this, you'll generate a blank report.

Use `pytest` if you don't want to generate a report :

```sh
pipenv run pytest -v -s
```
