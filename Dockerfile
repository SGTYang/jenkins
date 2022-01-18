FROM python:3.7.7-slim

WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py /microservices/
COPY requirements.txt /microservices/
COPY templates /microservices/
COPY static /microservices/


WORKDIR /microservices
EXPOSE 4321

CMD ["python", "app.py", "4321"]
