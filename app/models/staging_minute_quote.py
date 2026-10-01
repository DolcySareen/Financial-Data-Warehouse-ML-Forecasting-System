from app import db
from sqlalchemy import Column, String, Numeric, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

#Base = declarative_base()

class StagingMinuteQuote(db.Model):
    """
    A staging table for minute-level stock quotes. Records are appended, not overwritten.
    """
    __tablename__ = "staging_minute_quote"

    symbol = Column(String, primary_key=True)  # The stock symbol, e.g., AAPL
    name = Column(String, nullable=True)  # Company or asset name
    price = Column(Numeric, nullable=True)  # Current price
    change_percentage = Column(Numeric, nullable=True)  # Percent change
    change = Column(Numeric, nullable=True)  # Absolute change
    day_low = Column(Numeric, nullable=True)  # Lowest price of the day
    day_high = Column(Numeric, nullable=True)  # Highest price of the day
    year_high = Column(Numeric, nullable=True)  # Highest price in the year
    year_low = Column(Numeric, nullable=True)  # Lowest price in the year
    market_cap = Column(Numeric, nullable=True)  # Market capitalization
    price_average_50 = Column(Numeric, nullable=True)  # 50-day moving average
    price_average_200 = Column(Numeric, nullable=True)  # 200-day moving average
    exchange = Column(String, nullable=True)  # Exchange name
    volume = Column(BigInteger, nullable=True)  # Current volume
    average_volume = Column(BigInteger, nullable=True)  # Average daily volume
    open = Column(Numeric, nullable=True)  # Opening price of the day
    previous_close = Column(Numeric, nullable=True)  # Closing price of the previous day
    eps = Column(Numeric, nullable=True)  # Earnings per share
    pe = Column(Numeric, nullable=True)  # Price-to-earnings ratio
    shares_outstanding = Column(BigInteger, nullable=True)  # Number of shares outstanding

    @staticmethod
    def load_staging_minute_quote(session: Session, quote_data: dict) -> None:
        """
        Insert a new record into the staging minute quote table.
        If a record with the same symbol and timestamp exists, it will be skipped.

        :param session: SQLAlchemy session
        :param quote_data: Dictionary containing minute quote data
        """
        # Check if the record already exists based on the symbol and timestamp
        existing_record = session.query(StagingMinuteQuote).filter_by(
            symbol=quote_data["symbol"],
            timestamp=quote_data["timestamp"]
        ).one_or_none()

        if not existing_record:
            # Create a new record if one doesn't exist
            new_record = StagingMinuteQuote(
                symbol=quote_data["symbol"],
                name=quote_data.get("name"),
                price=quote_data.get("price"),
                change_percentage=quote_data.get("change_percentage"),
                change=quote_data.get("change"),
                day_low=quote_data.get("day_low"),
                day_high=quote_data.get("day_high"),
                year_high=quote_data.get("year_high"),
                year_low=quote_data.get("year_low"),
                market_cap=quote_data.get("market_cap"),
                price_average_50=quote_data.get("price_average_50"),
                price_average_200=quote_data.get("price_average_200"),
                exchange=quote_data.get("exchange"),
                volume=quote_data.get("volume"),
                average_volume=quote_data.get("average_volume"),
                open=quote_data.get("open"),
                previous_close=quote_data.get("previous_close"),
                eps=quote_data.get("eps"),
                pe=quote_data.get("pe"),
                shares_outstanding=quote_data.get("shares_outstanding"),
                timestamp=quote_data["timestamp"]
            )
            session.add(new_record)
            session.commit()  # Commit the new record to the database
