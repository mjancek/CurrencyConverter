FROM python:3.7

WORKDIR /CurrencyConverter
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY CurrencyConverter/ CurrencyConverter/

ENV PYTHONPATH /CurrencyConverter

EXPOSE 8080
CMD python CurrencyConverter/api.py