from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session


class DimCommodity(db.Model):
    __tablename__ = "dim_commodity"

    sk_commodity_id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=True)
    name = Column(String, nullable=True)
    currency = Column(String, nullable=True)

    @staticmethod
    def load_dim_commodity(session: Session, commodity_data: dict) -> int:
        """
        Load or update a commodity record in the database.
        If a record with the same symbol exists, update it with the new data.
        Otherwise, create a new record.

        :param session: SQLAlchemy session
        :param commodity_data: Dictionary containing commodity data
        :return: Primary key of the commodity record
        """
        # Check if the commodity already exists based on the symbol
        existing = session.query(DimCommodity).filter_by(symbol=commodity_data["symbol"]).one_or_none()

        if existing:
            # Explicitly update the existing record
            existing.symbol = commodity_data.get("symbol")
            existing.name = commodity_data.get("name")
            existing.currency = commodity_data.get("currency")
            session.commit()
            return existing.sk_commodity_id

        # Explicitly insert a new record
        new_commodity = DimCommodity(
            symbol=commodity_data.get("symbol"),
            name=commodity_data.get("name"),
            currency=commodity_data.get("currency"),
        )
        session.add(new_commodity)
        session.commit()
        return new_commodity.sk_commodity_id
    def get_commodity_id(session: Session, symbol: str) -> int:
        """
        Get the primary key of a commodity based on the symbol.

        :param session: SQLAlchemy session
        :param symbol: Commodity symbol
        :return: Primary key of the commodity record
        """
        commodity = session.query(DimCommodity).filter_by(symbol=symbol).one_or_none()
        if commodity:
            return commodity.sk_commodity_id
        return None
