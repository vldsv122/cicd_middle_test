FROM python:3.8-slim-buster

RUN mkdir /work_path
COPY / /work_path

WORKDIR /work_path

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver"]

