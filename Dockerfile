FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /base_directory
WORKDIR /base_directory
ADD . /base_directory/
RUN apt-get update
RUN apt-get install -y python3
RUN pip install --upgrade pip
RUN apt-get install -y git
RUN git init
RUN apt-get install -y gcc python3-dev
RUN apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev
RUN apt-get install -y default-mysql-client default-libmysqlclient-dev

RUN pip install mysqlclient  
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install pillow
RUN pip install requests
RUN pip install gunicorn
# RUN pip install -r requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]