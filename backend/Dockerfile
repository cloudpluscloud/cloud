FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary 

# COPY . ./
