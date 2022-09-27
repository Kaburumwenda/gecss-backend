FROM python:3.8.5-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# RUN pip install django
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install pillow
RUN pip install requests

COPY ./ /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

