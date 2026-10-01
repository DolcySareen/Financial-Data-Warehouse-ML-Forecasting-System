from app import db
from sqlalchemy import Column, Integer, String, Numeric, DateTime, BigInteger
from sqlalchemy.orm import Session

class DimStock(db.Model): # Update once per 6 hrs
    __tablename__ = "dim_stock"

    sk_stock_id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String)
    company_name = Column(String)
    currency = Column(String)
    sector = Column(String)
    exchange = Column(String)
    cik = Column(String)
    isin = Column(String)
    cusip = Column(String)
    industry = Column(String)
    country = Column(String)
    full_time_employees = Column(Integer)
    city = Column(String)
    state = Column(String)
    ipo_date = Column(DateTime)
    beta = Column(Numeric)
    return_on_equity = Column(Numeric)
    shares_outstanding = Column(BigInteger)
    earnings_announcement = Column(String)
    dividend_yield = Column(Numeric)
    debt_equity_ratio = Column(Numeric)
    price_to_book_ratio = Column(Numeric)
    cash_flow_per_share = Column(Numeric)
    peg_ratio = Column(Numeric)
    net_income = Column(Numeric) # previous 4 quarters

    def load_dim_stock(session: Session, company_data: dict) -> int:

        existing = session.query(DimStock).filter_by(symbol=company_data["symbol"]).one_or_none()
        if existing:
            for key, value in company_data.items():
                setattr(existing, key, value)
            session.commit()
            return existing.sk_stock_id

        new_company = DimStock(
            symbol=company_data["symbol"],
            beta=company_data.get("beta"),
            return_on_equity=company_data.get("return_on_equity"),
            shares_outstanding=company_data.get("shares_outstanding"),
            earnings_announcement=company_data.get("earnings_announcement"),
            dividend_yield=company_data.get("dividend_yield"),
            debt_equity_ratio=company_data.get("debt_equity_ratio"),
            price_to_book_ratio=company_data.get("price_to_book_ratio"),
            cash_flow_per_share=company_data.get("cash_flow_per_share"),
            peg_ratio=company_data.get("peg_ratio"),
            net_income=company_data.get("net_income"),
            company_name=company_data.get("company_name"),
            currency=company_data.get("currency"),
            sector=company_data.get("sector"),
            exchange=company_data.get("exchange"),
            cik=company_data.get("cik"),
            isin=company_data.get("isin"),
            cusip=company_data.get("cusip"),
            industry=company_data.get("industry"),
            country=company_data.get("country"),
            full_time_employees=company_data.get("full_time_employees"),
            city=company_data.get("city"),
            state=company_data.get("state"),
            ipo_date=company_data.get("ipo_date"),
        )

        session.add(new_company)
        session.commit()
        return new_company.sk_stock_id
    
    def get_stock_id(session, symbol):
        return session.query(DimStock).filter_by(symbol=symbol).one_or_none().sk_stock_id