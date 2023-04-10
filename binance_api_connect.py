from binance.spot import Spot as Client
from os import getenv
from dotenv import load_dotenv

from binance_api_classes import NewOrderParam

from binance.lib.utils import config_logging
import logging

config_logging(logging, logging.DEBUG)

BASE_URL = 'https://testnet.binance.vision'
client: Client


def main():
    # Load Private key and API key and Create client
    init()
    logging.info(client.exchange_info())
    params = NewOrderParam(
        symbol='BTCUSDT', quantity=0.001, price=28300).__dict__

    # placeTrade(params)


def placeTrade(params):
    response = client.new_order(**params)
    print(response)


def init():
    global client  # Assigning global variable
    load_dotenv()

    # Load the RSA private from .pem file
    PRIVATE_KEY = open("./binance-test-prv.pem").read()

    # Load API key from .env
    API_KEY = getenv("API_KEY")

    # Create the client
    client = Client(base_url=BASE_URL, api_key=API_KEY,
                    private_key=PRIVATE_KEY)


main()
