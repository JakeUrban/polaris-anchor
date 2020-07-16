FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y build-essential
WORKDIR /home
COPY ./app /home/

RUN pip install -r requirements.txt && python manage.py collectstatic --no-input

CMD python manage.py runserver --nostatic 0.0.0.0:8000
