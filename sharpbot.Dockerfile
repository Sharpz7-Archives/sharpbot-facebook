FROM python:3.6.6-alpine3.8

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install

WORKDIR /sharpbot

CMD ["pipenv", "run", "python", "-u", "client.py"]