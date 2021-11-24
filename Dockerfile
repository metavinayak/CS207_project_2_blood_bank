FROM alpine:latest

RUN apk add --update py3-pip
RUN apk add python3-dev
RUN apk add build-base

WORKDIR /usr/src/app/

COPY *.py ./
COPY requirements.txt ./
COPY hospital_data.sqlite ./
COPY templates/* ./templates/
COPY static/* ./static/

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 5000

CMD ["python3","main.py"]
