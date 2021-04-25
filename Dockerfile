FROM python:3.8

COPY . /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
