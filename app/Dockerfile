FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "app.main:app", "--workers", "4", "--worker-class","uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]