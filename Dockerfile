FROM python:3.8

WORKDIR /tmp

COPY . /tmp

ARG env_flask_variable=app/app 
ENV FLASK_APP=$env_flask_variable 

RUN pip install -r requirements.txt

