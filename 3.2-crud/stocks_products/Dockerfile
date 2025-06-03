FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache gcc musl-dev postgresql-dev python3-dev

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "stocks_products.wsgi:application", "--bind", "0.0.0.0:8000"]