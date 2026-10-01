from app.etl.extract.base_client import FMPClient

class HistoricalPrice(FMPClient):
    def __init__(self, api_key, date=None, open=None, high=None, low=None, close=None, adjClose=None,
                 volume=None, unadjustedVolume=None, change=None, changePercent=None, vwap=None, label=None,
                 changeOverTime=None):
        super().__init__(api_key)
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.adjClose = adjClose
        self.volume = volume
        self.unadjustedVolume = unadjustedVolume
        self.change = change
        self.changePercent = changePercent
        self.vwap = vwap
        self.label = label
        self.changeOverTime = changeOverTime
    def fetch(self, symbol, start_date=None, end_date=None):
        endpoint = f"v3/historical-price-full/{symbol}"
        params = {}
        if start_date and end_date:
            params['from'] = start_date.strftime('%Y-%m-%d')
            params['to'] = end_date.strftime('%Y-%m-%d')
        return self._make_request(endpoint, params)