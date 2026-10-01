import yaml
import json
import os

from app.etl.extract.endpoints.company import Company
from app.etl.extract.endpoints.exchange import Exchange
from app.etl.extract.endpoints.historical_price import HistoricalPrice
from app.etl.extract.endpoints.ratios import Ratios
from app.etl.extract.endpoints.stock_quote import StockQuote
from app.etl.extract.endpoints.exchange import Exchange
from app.etl.extract.endpoints.treasury_price import TreasuryPrice


def load_config(file_path):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config

class Extractor:
    def __init__(self, api_key, config_path, output_dir="output"):
        self.api_key = api_key
        self.config = load_config(config_path)
        self.output_dir = output_dir
        self._copy_config_stock_symbols()
    
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _save_to_file(self, category, symbol, data):

        file_path = f"{self.output_dir}/{category}_{symbol}.json"

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"Data for {symbol} in {category} saved to {file_path}.")

    def _copy_config_stock_symbols(self):
        self.config['symbols']['ratios'] = self.config['symbols']['stocks']
        self.config['symbols']['company'] = self.config['symbols']['stocks']

    # def fetch_all(self, start_date=None, end_date=None):
    #     fmp_client_classes = {
    #         "stocks_historical": HistoricalPrice(self.api_key),
    #         "stocks_quote": StockQuote(self.api_key),
    #         "commodities": HistoricalPrice(self.api_key),
    #         "bonds": TreasuryPrice(self.api_key),
    #         "indexes": HistoricalPrice(self.api_key),
    #         "ratios": Ratios(self.api_key),
    #         "company": Company(self.api_key),
    #         "exchanges": ExchangeList(self.api_key)
    #     }
    #     all_data = {}
        
    #     for category, symbols in self.config['symbols'].items():
            
    #         client = fmp_client_classes.get(category)
    #         if not client:
    #             continue
    #         category_data = {}
    #         for symbol in symbols:
    #             print(f"Fetching data for {symbol} in {category} from {start_date} to {end_date}...")
    #             if isinstance(client, HistoricalPrice) or isinstance(client, TreasuryPrice):
    #                 data = client.fetch(symbol, start_date=start_date, end_date=end_date)
    #             else:
    #                 data = client.fetch(symbol)  # Ratios and other categories don't use date range
                
    #             # Save the data to a file
    #             category_data[symbol] = data
    #         all_data[category] = category_data
    #     return all_data
    

    def fetch_historical(self, symbol, start_date=None, end_date=None):
        client = HistoricalPrice(self.api_key)
        return self._fetch_with_date_range(client, symbol, start_date, end_date)

    def fetch_quote(self, symbol):
        client = StockQuote(self.api_key)
        return self._fetch_without_date_range(client, symbol)

    def fetch_bonds(self, symbol, start_date=None, end_date=None):
        client = TreasuryPrice(self.api_key)
        return self._fetch_with_date_range(client, symbol, start_date, end_date)

    def fetch_ratios(self, symbol):
        client = Ratios(self.api_key)
        return self._fetch_without_date_range(client, symbol)

    def fetch_company(self, symbol):
        client = Company(self.api_key)
        return self._fetch_without_date_range(client, symbol)

    def fetch_exchange(self, symbol):
        client = Exchange(self.api_key)
        return self._fetch_without_date_range(client, symbol)

    def _fetch_with_date_range(self, client, symbol, start_date, end_date):
        # print(f"Fetching data for {symbol} from {start_date} to {end_date}...")
        return client.fetch(symbol, start_date=start_date, end_date=end_date)

    def _fetch_without_date_range(self, client, symbol):
        # print(f"Fetching data for {symbol}...")
        return client.fetch(symbol)
