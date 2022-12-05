FROM python
MAINTAINER Spencer Lunt <oslunt@byu.edu>

ENV DockerHOME=/home/app/webapp
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME
COPY . $DockerHOME

#install deps

RUN apt-get update
RUN pip install django
RUN pip install mysqlclient

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
