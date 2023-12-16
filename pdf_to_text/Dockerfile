FROM python:3.11.4-bullseye
RUN mkdir /app
WORKDIR /app

RUN pip install pipenv safety

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --dev
RUN pipenv check
COPY . .

CMD ["pipenv", "run", "python", "app.py"]
EXPOSE 8080
