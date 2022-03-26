ARG VERSION=3.9.7
ARG TAG=slim
FROM python:${VERSION}-${TAG}

ENV PYTHONUNBUFFERED 1

# update packages including pip
RUN apt update && apt upgrade -y
# was necessary to install mysqlclient at least on m1 docker
RUN apt install default-libmysqlclient-dev gcc -y
RUN pip install --upgrade pip

# copy necessary files
COPY ./ /code

# install necessary python packages
WORKDIR /code
RUN pip install -r requirements.txt

# run it actually
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
