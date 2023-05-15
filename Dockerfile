FROM python:3.9-alpine

WORKDIR /app

RUN apk add git

RUN pip install git+https://github.com/EnokiUN/voltage

COPY . .


CMD ["python3", "bot.py"]