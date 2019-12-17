# CurrencyConverter

Application take rates from European Central Bank. Rates are updated every day around 16:00 CET.


## Installation
Clone repository
```shell script
git clone https://github.com/mato0036/CurrencyConverter.git
```
##CLI application
To run CLI application, firstly install requirements for application
```shell script
pip install -r requirements.txt
```
Then run application
```shell script
python -m CurrencyConverter --amount <amount> --input_currency <3 letter name> [--output_currency <3 letter name or symbol>]
```

##API application
For API application is provided Docker image for easier use. 

To run API application build Docker image
```shell script
docker build -t CurrencyConverter-docker .
```
Then run image
```shell script
docker run -p 8080:8080 CurrencyConverter-docker
```
You can access application by opening in your browser
```
localhost:8080/currency_converter?amount=<amount>&input_currency=<3 letter name>&output_currency=<3letter name or symbol>
```

##Parameters
Parameter `input_currency` is not supporting symbols of currencies, because symbols are not exclusive for currencies.

However when is symbol used for `output_currency` application return all currencies, that have that symbol.
When `output_currency` is not provided, application converts to all supported currencies.
