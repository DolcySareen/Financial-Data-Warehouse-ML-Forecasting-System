from app.etl.extract.base_client import FMPClient

class SymbolList(FMPClient):
    def __init__(self, api_key, symbol=None, name=None, price=None, exchange=None, exchangeShortName=None, type=None):
        super().__init__(api_key)
        self.symbol = symbol
        self.name = name
        self.price = price
        self.exchange = exchange
        self.exchangeShortName = exchangeShortName
        self.type = type
    def fetch(self):
        endpoint = "v3/stock/list"
        return self._make_request(endpoint)