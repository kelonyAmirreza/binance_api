from error import ParamNotSupportedError

SYMBOLS = ('BTCUSDT', 'ETHUSDT')
SIDES = ('BUY', 'SELL')
TYPES = ('LIMIT', 'MARKET', 'STOP_LOSS', 'STOP_LOSS_LIMIT',
         'TAKE_PROFIT',  'TAKE_PROFIT_LIMIT')


def check_parameter(value, name):
    # if not value and value != 0:
    #     raise ParameterRequiredError([name])
    match name:
        case "symbol":
            if value.upper() not in SYMBOLS:
                raise ParamNotSupportedError(value)
        case "side":
            if value.upper() not in SIDES:
                raise ParamNotSupportedError(value)
        case "type":
            if value.upper() not in TYPES:
                raise ParamNotSupportedError(value)


def check_parameters(params):
    """Validate multiple parameters
    params = [
        ['btcusdt', 'symbol'],
        [10, 'side']
    ]
    """
    for p in params:
        check_parameter(p[0], p[1])
