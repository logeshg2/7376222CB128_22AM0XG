# base image (slim version)
FROM python:3.9-slim

WORKDIR /Day1

COPY . /Day1

# pip dependinces
RUN pip install --no-cache-dir flask

# port number
EXPOSE 5000

# env variables
ENV FLASK_APP=sample.py

CMD ["flask","run","--host=0.0.0.0"]
