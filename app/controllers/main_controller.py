import os
import datetime
from dotenv import load_dotenv
from app.db_connection import connect_to_database
from app.etl.extract.extractor import Extractor
from app.etl.transform.transform import Transform
from app.models.dim_stock import DimStock
from app.models.dim_exchange import DimExchange
from app.models.dim_commodity import DimCommodity
from app.models.dim_index import DimIndex
from app.models.dim_bond import DimBond
from app.models.dim_date import DimDate
from app.models.fact_market_metrics import FactMarketMetrics
from app.models.bond_market_metrics import BondMarketMetrics
from app import db
#from db_connection import connect_to_database

load_dotenv()

PERIOD = 5 # years
API_KEY = os.getenv("FMP_API_KEY")
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.yaml')

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=PERIOD * 365)
extractor = Extractor(API_KEY, CONFIG_PATH)
stock_symbols = extractor.config['symbols']['stocks']
exchange_symbols = extractor.config['symbols']['exchanges']
commodity_symbols = extractor.config['symbols']['commodities']
index_symbols = extractor.config['symbols']['indexes']
bond_symbols = extractor.config['symbols']['bonds']

session = connect_to_database()

def execute_stock_data():
    # extractor.fetch_all(start_date=start_date, end_date=end_date)
    for symbol in stock_symbols:
        quote_data = extractor.fetch_quote(symbol)
        quote_data = quote_data[0]
        company_data = extractor.fetch_company(symbol)
        company_data = company_data[0]
        ratios_data = extractor.fetch_ratios(symbol)
        ratios_data = ratios_data[0]
        transformed_data = Transform.transform_stock_data(quote_data, company_data, ratios_data)
        DimStock.load_dim_stock(company_data=transformed_data, session=session)
        # print(transformed_data)

def execute_exchange_data():
    for symbol in exchange_symbols:
        exchange_data = extractor.fetch_exchange(symbol)
        transformed_data = Transform.transform_exchange_data(symbol, exchange_data)
        DimExchange.load_dim_exchange(exchange_data=transformed_data, session=session)
        # print(transformed_data)  

def execute_commodity_data():
    for symbol in commodity_symbols:
        commodity_data = extractor.fetch_quote(symbol)
        commodity_data = commodity_data[0]
        transformed_data = Transform.transform_commodity_data(commodity_data)
        DimCommodity.load_dim_commodity(commodity_data=transformed_data, session=session)
        print(transformed_data)

def execute_index_data():
    for symbol in index_symbols:
        index_data = extractor.fetch_quote(symbol)
        index_data = index_data[0]
        transformed_data = Transform.transform_index_data(index_data)
        DimIndex.load_dim_index(index_data=transformed_data, session=session)

def execute_bond_data():
    for symbol in bond_symbols:
        transformed_data = {
            "treasury_name": symbol
        }
        DimBond.load_dim_bond(bond_data=transformed_data, session=session)

        
def execute_fact_historical():
    pass

def execute_fact_hourly():
    symbols = stock_symbols + commodity_symbols + index_symbols
    for symbol in symbols:
        print(symbol)
        quote_data = extractor.fetch_quote(symbol)
        quote_data = quote_data[0]
        # print(quote_data)
        timestamp = quote_data.get("timestamp")
        transformed_date = Transform.transform_date_data(timestamp)
        # print(transformed_date)
        date_fk = DimDate.load_dim_date(date_data=transformed_date, session=session)
        transformed_data = Transform.transform_fact(quote_data)
        transformed_data['fk_date_id'] = date_fk
        if symbol in stock_symbols:
            transformed_data['fk_stock_id'] = DimStock.get_stock_id(session, symbol)
        elif symbol in commodity_symbols:
            transformed_data['fk_commodity_id'] = DimCommodity.get_commodity_id(session, symbol)
        elif symbol in index_symbols:
            transformed_data['fk_index_id'] = DimIndex.get_index_id(session, symbol)
        FactMarketMetrics.load_fact_market_metrics(metrics_data=transformed_data, session=session)
        print(transformed_data)

def execute_bond_metrics():
    for symbol in bond_symbols:
        bond_data = extractor.fetch_bonds(symbol, start_date, end_date)
        for bond_item in bond_data:
            timestamp = datetime.datetime.strptime(bond_item['date'], '%Y-%m-%d').timestamp()
            transformed_date = Transform.transform_date_data(timestamp)
            # print(transformed_date)
            date_fk = DimDate.load_dim_date(date_data=transformed_date, session=session)
            transformed_data = Transform.transform_bond_metrics(bond_item)
            transformed_data['fk_date_id'] = date_fk
            transformed_data['fk_bond_id'] = DimBond.get_bond_id(session, symbol)
            # print(transformed_data)
            BondMarketMetrics.load_bond_market_metrics(session, transformed_data)

if __name__ == "__main__":
    execute_stock_data()