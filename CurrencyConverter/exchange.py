from CurrencyConverter.currencies import curr_symbols


# Check if symbol is one of supported currencies
# If so, return list of all currencies with that symbol
def check_symbol(curr):
    curr_list = []
    for key, value in curr_symbols.items():
        if curr == value:
            curr_list.append(key)
    return curr_list


# Check if currency is supported and return currency or false
def is_supported(curr, currencies):
    if curr in currencies.keys():
        return curr
    return False


# Check if currencies are supported and find all currencies with given symbol
# Return dictionary with all parameters
def check_currencies(args, currencies):
    input_curr = is_supported(args['input_currency'], currencies)
    # Check if is field empty or not supported currency
    if not input_curr:
        if args['input_currency']:
            raise ValueError('{} is not supported, try to use correct 3 letter currency name'.format(args['input_currency']))
        else:
            raise ValueError('Provide input currency')

    output_curr = check_symbol(args['output_currency'])
    # Do the same check with output currency plus if user did not provide output currency, it is set to 'all'
    if not output_curr:
        if args['output_currency'] == 'all':
            output_curr = args['output_currency']
        else:
            output_curr = is_supported(args['output_currency'], currencies)
        if not output_curr:
            if args['output_currency']:
                raise ValueError('{} is not supported, try to use correct 3 letter currency name'.format(args['output_currency']))
            else:
                raise ValueError('Provide output currency')

    amount = args['amount']

    return {'amount': amount, 'input_currency': input_curr, 'output_currency': output_curr}


# Change currencies to provided currencies
def change_currency(input_info, currencies):
    # We have currency rates to euro, so firstly change input currency to euro
    if input_info['input_currency'] != 'EUR':
        input_currency_amount_EUR = input_info['amount'] / float(currencies[input_info['input_currency']])
    else:
        input_currency_amount_EUR = float(input_info['amount'])

    # Add all output currencies to dictionary with value
    output = {}
    if input_info['output_currency'] == 'all':
        for curr, rate in currencies.items():
            output[curr] = float("{0:.2f}".format(input_currency_amount_EUR * float(rate)))
        output['EUR'] = float("{0:.2f}".format(input_currency_amount_EUR))
    else:
        if isinstance(input_info['output_currency'], str):
            output[input_info['output_currency']] = float("{0:.2f}".format(input_currency_amount_EUR * float(currencies[input_info['output_currency']])))
        else:
            for curr in input_info['output_currency']:
                output[curr] = float("{0:.2f}".format(input_currency_amount_EUR * float(currencies[curr])))

    return {
        "input": {
            "amount": input_info['amount'],
            "currency": input_info['input_currency']
        },
        "output": output
    }