FROM python:3.7.7-slim

WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY frontend/app.py /app/
COPY requirements.txt /app/
COPY frontend/templates /app/templates
COPY frontend/static /app/static

EXPOSE 80
WORKDIR /app

CMD ["python", "app.py", "80"]
