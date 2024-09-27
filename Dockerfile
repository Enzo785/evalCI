FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8


WORKDIR /app

COPY ./app /app

RUN pip install --upgrade pip & pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
