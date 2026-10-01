from app.etl.extract.base_client import FMPClient

class StockQuote(FMPClient):
    def __init__(self,
                 api_key,
                 symbol=None,
                 name=None,
                 price=None,
                 changesPercentage=None,
                 change=None,
                 dayLow=None,
                 dayHigh=None,
                 yearHigh=None,
                 yearLow=None,
                 marketCap=None,
                 priceAvg50=None,
                 priceAvg200=None,
                 exchange=None,
                 volume=None,
                 avgVolume=None,
                 open=None,
                 previousClose=None,
                 eps=None,
                 pe=None,
                 earningsAnnouncement=None,
                 sharesOutstanding=None,
                 timestamp=None):
        super().__init__(api_key)
        self.symbol = symbol
        self.name = name
        self.price = price
        self.changesPercentage = changesPercentage
        self.change = change
        self.dayLow = dayLow
        self.dayHigh = dayHigh
        self.yearHigh = yearHigh
        self.yearLow = yearLow
        self.marketCap = marketCap
        self.priceAvg50 = priceAvg50
        self.priceAvg200 = priceAvg200
        self.exchange = exchange
        self.volume = volume
        self.avgVolume = avgVolume
        self.open = open
        self.previousClose = previousClose
        self.eps = eps
        self.pe = pe
        self.earningsAnnouncement = earningsAnnouncement
        self.sharesOutstanding = sharesOutstanding
        self.timestamp = timestamp

    def fetch(self, symbol):
        endpoint = f"v3/quote/{symbol}"
        params = {}
        return self._make_request(endpoint, params)