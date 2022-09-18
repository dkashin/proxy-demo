FROM python:3.10-alpine

ENV PATH=/root/.local/bin:$PATH

WORKDIR /proxy-demo

COPY requirements.txt .
COPY ./proxy ./proxy
COPY ./templates ./templates
COPY proxy_uwsgi.ini .

RUN apk add gcc build-base linux-headers shadow
RUN pip install --user -r requirements.txt
RUN mkdir -p logs
RUN mkdir -p db

EXPOSE 8080

CMD uwsgi --http :8080 proxy_uwsgi.ini
