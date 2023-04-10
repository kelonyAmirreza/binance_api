class NewOrderParam:

    def __init__(self, symbol: str, quantity: float, price: float, side: str = 'BUY', type: str = 'LIMIT', timeInForce: str = 'GTC') -> None:
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.side = side
        self.type = type
        self.timeInForce = timeInForce
