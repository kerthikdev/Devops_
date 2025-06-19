FROM alpine:3.12

WORKDIR /app
COPY ./app /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "main.py"]
