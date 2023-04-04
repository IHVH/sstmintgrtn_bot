FROM python:3.11-bullseye
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
COPY config/ ./config
COPY res/ ./res
RUN ls 
RUN ls /code
CMD [ "python", "./app.py" ]