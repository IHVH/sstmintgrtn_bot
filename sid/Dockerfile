FROM python:3.10.7-bullseye
WORKDIR /code
COPY sid/requirements.txt .
RUN pip install -r requirements.txt
COPY sid/ .
COPY sid/json/ ./json
CMD [ "python", "./bot.py" ]