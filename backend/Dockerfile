FROM python:3.11-slim

WORKDIR /carfeeling

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "run:app"]
