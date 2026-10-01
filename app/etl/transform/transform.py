
from datetime import datetime
import re
#import extractor
from app.etl.extract.extractor import Extractor

class Transform:

    @staticmethod
    def transform_exchange_data(symbol, exchange_data):
        """
        Transforms raw exchange data fetched from the ExchangeList class into a structured format
        for loading into the DimExchange table.
        :param raw_exchange_data: Dictionary containing raw exchange data from the API
        :return: Transformed exchange data dictionary
        """
        opening_hour = exchange_data.get('stockMarketHours', {}).get('openingHour', None)
        closing_hour = exchange_data.get('stockMarketHours', {}).get('closingHour', None)
        print(f"Opening hour: {opening_hour}")
        timezone = re.search(r'([A-Za-z]+|[-+]\d{2})$', opening_hour).group(1)

        opening_hour = re.sub(r'\s+[A-Za-z]+$', '', opening_hour)
        closing_hour = re.sub(r'\s+[A-Za-z]+$', '', closing_hour)
        transformed_data = {
        "name": exchange_data.get("stockExchangeName", "").strip(),  # Normalize the name
        "symbol": symbol.strip().upper(),  # Ensure symbols are uppercase
        "opening_hour": opening_hour, # Clean opening hour
        "closing_hour": closing_hour, # Clean closing hour
        "timezone": timezone  # Normalize timezone
        }
        return transformed_data
    
    @staticmethod
    def transform_stock_data(quote_data, company_data, ratio_data):
        
        transformed_data = {
            "symbol": quote_data.get("symbol", "").strip().upper(),
            "company_name": company_data.get("companyName", "").strip(),
            "currency": company_data.get("currency", "").strip(),
            "sector": company_data.get("sector", "").strip(),
            "industry": company_data.get("industry", "").strip(),
            "country": company_data.get("country", "").strip(),
            "exchange": company_data.get("exchangeShortName", "").strip(),
            "full_time_employees": company_data.get("fullTimeEmployees"),
            "city": company_data.get("city", "").strip(),
            "state": company_data.get("state", "").strip(),
            "ipo_date": datetime.strptime(company_data.get("ipoDate", ""), "%Y-%m-%d") if company_data.get("ipoDate") else None,
            "cik": company_data.get("cik"),
            "isin": company_data.get("isin"),
            "cusip": company_data.get("cusip"),
            "beta": company_data.get("beta"),
            "return_on_equity": ratio_data.get("returnOnEquity"),
            "shares_outstanding": quote_data.get("sharesOutstanding"),
            "earnings_announcement": quote_data.get("earningsAnnouncement"),
            "dividend_yield": ratio_data.get("dividendYield"),
            "debt_equity_ratio": ratio_data.get("debtEquityRatio"),
            "price_to_book_ratio": ratio_data.get("priceToBookRatio"),
            "cash_flow_per_share": ratio_data.get("operatingCashFlowPerShare"),
            "peg_ratio": ratio_data.get("priceEarningsToGrowthRatio"),
            "net_income": ratio_data.get("netProfitMargin")
        }
        return transformed_data
    
    @staticmethod
    def transform_date_data(timestamp):
        """
        Transform timestamp from quote_data into a structured dictionary for DimDate.

        :param quote_data: Dictionary containing stock quote data with a timestamp.
        :return: Dictionary with derived date fields.
        """
        if not timestamp:
            return None  # Handle missing timestamp gracefully

        # Parse the timestamp
        dt = datetime.fromtimestamp(int(timestamp))

        # Compute derived fields
        transformed_date_data = {
            "full_date": dt.replace(second=0, microsecond=0),
            "hour": dt.hour,
            "minute": dt.minute,
            "day_of_week": dt.weekday(),  # Monday is 0, Sunday is 6
            "day_name": dt.strftime("%A"),  # Full day name
            "day_of_month": dt.day,
            "day_of_year": dt.timetuple().tm_yday,
            "week_of_year": dt.isocalendar().week,
            "month": dt.month,
            "month_name": dt.strftime("%B"),  # Full month name
            "quarter": (dt.month - 1) // 3 + 1,
            "year": dt.year,
            "fiscal_year": dt.year if dt.month >= 4 else dt.year - 1,  # Fiscal year starting in April
            "is_weekend": dt.weekday() in [5, 6],  # True if Saturday or Sunday
            "am_pm": "AM" if dt.hour < 12 else "PM"
        }

        return transformed_date_data
   
    @staticmethod
    def transform_bond_data():
        bond_data = {
            "sk_bond_id": 1,
            "treasury_name": 'US_Treasury'
        }
        return bond_data
    
    @staticmethod
    def transform_index_data(index_data):
        transformed_data = {
            "name": index_data.get("name", "").strip(),  # Normalize the name
            "symbol": index_data.get("symbol", "").strip().upper(),  # Ensure symbols are uppercase
            "currency": "USD"  # All prices are in USD
        }
        return transformed_data

    @staticmethod
    def transform_commodity_data(commodity_data):
         
         transformed_data = {
            "name": commodity_data.get("name", "").strip(),  # Normalize the name
            "symbol": commodity_data.get("symbol", "").strip().upper(),  # Ensure symbols are uppercase
            "currency" : "USD" # All prices are in USD
            }
         return transformed_data

    @staticmethod
    def transform_fact(stock_data):  
        transformed_data = {
            "symbol": stock_data.get("symbol", "").strip().upper(),
            "current_price": stock_data.get("price"),
            "market_cap": stock_data.get("marketCap"),
            "volume": stock_data.get("volume"),
            "eps": stock_data.get("eps"), #calculate for historical
            "pe": stock_data.get("pe"), #calculate for historical
            "vwap": stock_data.get("vwap") #calculate
        }  
        return transformed_data

    @staticmethod
    def transform_bond_metrics(bond_data):
        transformed_data = {
            "fk_bond_id": bond_data.get("fk_bond_id"),
            "fk_date_id": bond_data.get("fk_date_id"),
            "m1_month": bond_data.get("month1"),
            "m2_month": bond_data.get("month2"),
            "m3_month": bond_data.get("month3"),
            "m6_month": bond_data.get("month6"),
            "m1_year": bond_data.get("year1"),
            "m2_year": bond_data.get("year2"),
            "m3_year": bond_data.get("year3"),
            "m5_year": bond_data.get("year5"),
            "m7_year": bond_data.get("year7"),
            "m10_year": bond_data.get("year10"),
            "m20_year": bond_data.get("year20"),
            "m30_year": bond_data.get("year30")
        }
        return transformed_data
