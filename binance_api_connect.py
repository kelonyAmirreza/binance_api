from binance.spot import Spot as Client
from os import getenv
from dotenv import load_dotenv

load_dotenv()

PRIVATE_KEY = open("./binance-test-prv.pem").read()
API_KEY = getenv("API_KEY")
print(API_KEY)

client = Client(base_url='https://testnet.binance.vision', api_key=API_KEY)
print(client.time())
