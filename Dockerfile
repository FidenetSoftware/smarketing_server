FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade --force-reinstall -r requirements.txt
RUN pip list


COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]


