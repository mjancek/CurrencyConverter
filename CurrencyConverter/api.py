from flask import Flask, jsonify, request
from CurrencyConverter import currency_converter

app = Flask(__name__)


@app.route("/currency_converter")
def return_api():
    # Parse arguments from GET method
    args = {'amount': request.args.get('amount', type=float),
            'input_currency': request.args.get('input_currency', type=str),
            'output_currency': request.args.get('output_currency', type=str, default='all')}
    # Run program and check if there was some error
    try:
        response = currency_converter.main(args)
    except ValueError as err:
        return jsonify({"error": err.args}), 400
    except ConnectionError as err:
        return jsonify({'error': err.args}), 503
    except TimeoutError as err:
        return jsonify({'error': err.args}), 504
    else:
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="localhost")

