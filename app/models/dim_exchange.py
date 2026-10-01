from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

class DimExchange(db.Model):
    """
    Dimension table for storing exchange metadata.
    """
    __tablename__ = "dim_exchange"

    sk_exchange_id = Column(Integer, primary_key=True, autoincrement=True)  # Surrogate key
    name = Column(String, nullable=False)  # Name of the exchange, e.g., "New York Stock Exchange"
    symbol = Column(String, nullable=False, unique=True)  # Exchange symbol, e.g., "NYSE"
    opening_hour = Column(String, nullable=True)  # Opening hour of the exchange
    closing_hour = Column(String, nullable=True)  # Closing hour of the exchange
    timezone = Column(String, nullable=True)  # Timezone of the exchange

    @staticmethod
    def load_dim_exchange(session: Session, exchange_data: dict) -> int:
        """
        Load or update an exchange record in the database.
        If a record with the same symbol exists, update it with the new data.
        Otherwise, create a new record.

        :param session: SQLAlchemy session
        :param exchange_data: Dictionary containing exchange data
        :return: Primary key of the exchange record
        """
        # Check if the exchange already exists based on the symbol
        existing = session.query(DimExchange).filter_by(symbol=exchange_data["symbol"]).one_or_none()

        if existing:
            # Update the existing record with new data
            for field, value in exchange_data.items():
                if hasattr(existing, field) and value is not None:
                    setattr(existing, field, value)
            session.commit()  # Save changes to the database
            return existing.sk_exchange_id

        # If the exchange does not exist, create a new record
        new_exchange = DimExchange(
            name=exchange_data["name"],
            symbol=exchange_data["symbol"],
            opening_hour=exchange_data.get("opening_hour"),
            closing_hour=exchange_data.get("closing_hour"),
            timezone=exchange_data.get("timezone")
        )
        session.add(new_exchange)
        session.commit()  # Save the new record to the database
        return new_exchange.sk_exchange_id
