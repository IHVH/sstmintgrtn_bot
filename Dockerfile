FROM python:3.11-bullseye
WORKDIR /code
RUN pip install -r requirements.txt
WORKDIR /code/src
RUN ls 
RUN ls /code
CMD [ "python", "./app.py" ]