FROM alpine:latest

RUN apk add --update py3-pip
RUN apk add python3-dev
RUN apk add build-base

COPY *.py /usr/src/app/
COPY requirements.txt /usr/src/app/
COPY hospital_data.sqlite /usr/src/app/
COPY templates/* /usr/src/app/templates/
COPY static/* /usr/src/app/static/

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

EXPOSE 5000

CMD ["python3","/usr/src/app/main.py"]
