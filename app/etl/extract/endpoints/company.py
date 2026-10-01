from app.etl.extract.base_client import FMPClient

class Company(FMPClient):
    def __init__(self, api_key, symbol=None, price=None, beta=None, volAvg=None, mktCap=None, lastDiv=None, range_=None, changes=None, companyName=None, currency=None, cik=None,
                 isin=None, cusip=None, exchange=None, exchangeShortName=None, industry=None, website=None, description=None, ceo=None, sector=None, country=None,
                 fullTimeEmployees=None, phone=None, address=None, city=None, state=None, zip_=None, dcfDiff=None, dcf=None, image=None, ipoDate=None, defaultImage=None,
                 isEtf=None, isActivelyTrading=None, isAdr=None, isFund=None):
        super().__init__(api_key)
        self.symbol = symbol
        self.price = price
        self.beta = beta
        self.volAvg = volAvg
        self.mktCap = mktCap
        self.lastDiv = lastDiv
        self.range = range_
        self.changes = changes
        self.companyName = companyName
        self.currency = currency
        self.cik = cik
        self.isin = isin
        self.cusip = cusip
        self.exchange = exchange
        self.exchangeShortName = exchangeShortName
        self.industry = industry
        self.website = website
        self.description = description
        self.ceo = ceo
        self.sector = sector
        self.country = country
        self.fullTimeEmployees = fullTimeEmployees
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_
        self.dcfDiff = dcfDiff
        self.dcf = dcf
        self.image = image
        self.ipoDate = ipoDate
        self.defaultImage = defaultImage
        self.isEtf = isEtf
        self.isActivelyTrading = isActivelyTrading
        self.isAdr = isAdr
        self.isFund = isFund

    def fetch(self, symbol):
        endpoint = f"v3/profile/{symbol}"
        return self._make_request(endpoint)