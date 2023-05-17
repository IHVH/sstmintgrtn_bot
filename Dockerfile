FROM python:3.11-bullseye
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY / .
RUN ls /code
RUN ls /code/src
CMD [ "python", "./src/app.py" ]