from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

class DimIndex(db.Model):
    """
    Dimension table for storing index metadata.
    """
    __tablename__ = "dim_index"

    sk_index_id = Column(Integer, primary_key=True, autoincrement=True)  # Surrogate key
    symbol = Column(String, nullable=True)  # Index symbol, e.g., SPX
    name = Column(String, nullable=True)  # Full name of the index
    currency = Column(String, nullable=True)  # Currency of the index, e.g., USD

    @staticmethod
    def load_dim_index(session: Session, index_data: dict) -> int:
        """
        Load or update an index record in the database.
        If a record with the same symbol exists, update it with the new data.
        Otherwise, create a new record.

        :param session: SQLAlchemy session
        :param index_data: Dictionary containing index data
        :return: Primary key of the index record
        """
        # Check if the index already exists based on the symbol
        existing = session.query(DimIndex).filter_by(symbol=index_data["symbol"]).one_or_none()

        if existing:
            # Update the existing record with new data
            for field, value in index_data.items():
                if hasattr(existing, field) and value is not None:
                    setattr(existing, field, value)
            session.commit()  # Save changes to the database
            return existing.sk_index_id

        # If the index does not exist, create a new record
        new_index = DimIndex(
            symbol=index_data["symbol"],
            name=index_data.get("name"),
            currency=index_data.get("currency")
        )
        session.add(new_index)
        session.commit()  # Save the new record to the database
        return new_index.sk_index_id
    
    def get_index_id(session: Session, symbol: str) -> int:
        """
        Get the primary key of an index based on the symbol.

        :param session: SQLAlchemy session
        :param symbol: Index symbol
        :return: Primary key of the index record
        """
        index = session.query(DimIndex).filter_by(symbol=symbol).one_or_none()
        if index:
            return index.sk_index_id
        return None