from CurrencyConverter import parser
from CurrencyConverter import get_data
from CurrencyConverter import exchange


def main(args):
    # Get xml data
    try:
        xml = get_data.get_xml()
    except ConnectionError:
        raise
    except TimeoutError:
        raise
    except ResourceWarning:
        raise
    # Parse xml to dictionary
    currencies = parser.parse_xml(xml)
    # Check if currencies are supported
    try:
        args_parsed = exchange.check_currencies(args, currencies)
    except ValueError:
        raise
    # Change currencies and create response
    response = exchange.change_currency(args_parsed, currencies)
    return response


if __name__ == '__main__':
    args = parser.parse_arg()
    try:
        response = main(args)
    except Exception as err:
        print(err.args[0])
    else:
        print(response)
