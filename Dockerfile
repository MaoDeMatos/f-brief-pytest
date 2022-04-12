FROM python:3.10-slim as final

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install

# Test and generate a report in the container
RUN pipenv run test

# ENTRYPOINT [ "pipenv" ]

CMD pipenv run flask run
