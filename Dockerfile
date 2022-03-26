ARG VERSION=3.9.7
ARG TAG=slim
FROM python:${VERSION}-${TAG}

ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y

RUN pip install --upgrade pip

COPY ./ /code

WORKDIR /code
RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
