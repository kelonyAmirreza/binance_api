from binance.spot import Spot as Client
from os import getenv
from dotenv import load_dotenv

from utils import check_parameters


BASE_URL = 'https://testnet.binance.vision'
PRIVATE_KEY_ADDRESS = './binance-test-prv.pem'
client: Client


def main():
    # Load Private key and API key and Create client
    init()
    print(client.account(), end='\n\n')

    success = placeTrade(symbol='btcusdt', quantity=0.001,
                         price=28400, side='SELL')
    if success:
        print("Order submitted!\n\n")

    print(client.get_open_orders(None))
    # client.cancel_open_orders('BTCUSDT')


def placeTrade(symbol: str, quantity: float, price: float, side: str = 'BUY', type: str = 'LIMIT', timeInForce: str = 'GTC', **kwargs) -> bool:
    """New Order (TRADE)

    Post a new order

    POST /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

    Args:
        symbol (str)
        quantity (float)
        price (float)
        side (str)
        type (str)
    Keyword Args:
        timeInForce (str, optional)
        quantity (float, optional)
        quoteOrderQty (float, optional)
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        strategyId (int, optional)
        strategyType (int, optional): The value cannot be less than 1000000.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    try:
        check_parameters(
            [[symbol, "symbol"], [side, "side"], [type, "type"]])

        symbol = symbol.upper()
        client.new_order(symbol=symbol, quantity=quantity,
                         price=price, side=side, type=type, timeInForce=timeInForce, **kwargs)

        print(
            f'{type} order submited for {symbol} pair.\nFor: {quantity}\nat price: {price}')
        return True
    except:
        return False


def init():
    global client  # Assigning global variable
    load_dotenv()

    # Load the RSA private from .pem file
    PRIVATE_KEY = open(PRIVATE_KEY_ADDRESS).read()

    # Load API key from .env
    API_KEY = getenv("API_KEY")

    # Create the client
    client = Client(base_url=BASE_URL, api_key=API_KEY,
                    private_key=PRIVATE_KEY)


main()
