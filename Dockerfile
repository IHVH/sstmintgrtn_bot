FROM python:3.11-bullseye
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
#COPY src/ .
WORKDIR /code/src
RUN ls /
RUN ls /code/src
CMD [ "python", "app.py" ]