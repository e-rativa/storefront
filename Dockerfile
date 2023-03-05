#FROM python:3.9.16-alpine3.16
FROM python:3.9.7-slim-buster

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
# cambiar el puerto
CMD [ "python", "./entrypoint.py"]
EXPOSE 5000
