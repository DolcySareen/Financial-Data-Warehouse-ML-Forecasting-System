from app.etl.extract.base_client import FMPClient

class Exchange(FMPClient):
    def __init__(self, api_key, 
                stockExchangeName=None, stockMarketHours=None, stockMarketHolidays=None, 
                isTheStockMarketOpen=False, isTheEuronextMarketOpen=False, isTheForexMarketOpen=True, 
                isTheCryptoMarketOpen=True):
        super().__init__(api_key)
        self.stockExchangeName = stockExchangeName
        self.stockMarketHours = stockMarketHours
        self.stockMarketHolidays = stockMarketHolidays
        self.isTheStockMarketOpen = isTheStockMarketOpen
        self.isTheEuronextMarketOpen = isTheEuronextMarketOpen
        self.isTheForexMarketOpen = isTheForexMarketOpen
        self.isTheCryptoMarketOpen = isTheCryptoMarketOpen

    def fetch(self, symbol):
        endpoint = "v3/is-the-market-open"
        return self._make_request(endpoint,params={"exchange": symbol})