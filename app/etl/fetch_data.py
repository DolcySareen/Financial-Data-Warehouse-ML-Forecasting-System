import os
import datetime
from extract.extractor import Extractor
from dotenv import load_dotenv
from transform import Transform

load_dotenv()

PERIOD = 5 # years
API_KEY = os.getenv("FMP_API_KEY")
CONFIG_PATH = "config.yaml"

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=PERIOD * 365)
extractor = Extractor(API_KEY, CONFIG_PATH)
symbols = extractor.config['symbols']['stocks']

def execute_stock_data():
    # extractor.fetch_all(start_date=start_date, end_date=end_date)
    print(symbols)
    for symbol in symbols:
        stock_data = extractor.fetch_quote(symbol)
        company_data = extractor.fetch_company(symbol)
        ratios_data = extractor.fetch_ratios(symbol)
        transformed_data = Transform.transfor_fact(stock_data, company_data, ratios_data)
        loader.load_fact(transformed_data)

def execute_bond_data():
    transformed_data = Transform.transform_bond()
    loader.load_bond(bond_data)
    
def execute_exchange_date():
    for symbol in symbols:
        exchange_data = extractor.fetch_exchanges(symbol)
        transformed_data = Transform.transform_commodity_data(symbol, exchange_data)
        #loader

def execute_commodity_data():
    for symbol in symbols:
        commodity_data = extractor.fetch_commodities(symbol)
        transformed_data = Transform.transform_commodity_data(commodity_data)
        #loader.....

def execute_index_data():
    for symbol in symbols:
        index_data = extractor.fetch
        transformed_data = Transform.transform_commodity_data(commodity_data)
        #loader.....
        
def execute_fact_historical():
    pass

def execute_fact_hourly():

    pass

if __name__ == "__main__":
    run_extraction()