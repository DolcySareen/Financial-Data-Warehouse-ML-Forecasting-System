from app.etl.extract.base_client import FMPClient

class TreasuryPrice(FMPClient):
    def __init__(self, api_key, date=None, month1=None, month2=None, month3=None, month6=None, year1=None, 
                 year2=None, year3=None, year5=None, year7=None, year10=None, year20=None, year30=None):
        super().__init__(api_key)
        self.date = date
        self.month1 = month1
        self.month2 = month2
        self.month3 = month3
        self.month6 = month6
        self.year1 = year1
        self.year2 = year2
        self.year3 = year3
        self.year5 = year5
        self.year7 = year7
        self.year10 = year10
        self.year20 = year20
        self.year30 = year30
    def fetch(self, symbol, start_date=None, end_date=None):
        endpoint = f"v4/{symbol}"
        params = {}
        if start_date and end_date:
            params['from'] = start_date.strftime('%Y-%m-%d')
            params['to'] = end_date.strftime('%Y-%m-%d')
        return self._make_request(endpoint, params)