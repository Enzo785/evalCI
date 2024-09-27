FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8


WORKDIR /app

COPY . /app

RUN pip install --upgrade pip & pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["uvicorn", "mini-groq:app", "--host", "0.0.0.0", "--port", "8000"]
