FROM python:3.12-bullseye
#RUN apt-get update
#RUN apt-get install build-essential git -y
RUN pip install --upgrade pip

ENV PROJECT_ROOT /app

WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:8000
