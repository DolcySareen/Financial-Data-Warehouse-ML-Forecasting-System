from app import db
from sqlalchemy import Column, Integer, Numeric, BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship, Session

from app.models.dim_stock import DimStock
from app.models.dim_exchange import DimExchange
from app.models.dim_commodity import DimCommodity
from app.models.dim_index import DimIndex
from app.models.dim_date import DimDate

class FactMarketMetrics(db.Model):
    
    __tablename__ = "fact_market_metrics"

    sk_market_metrics_id = Column(Integer, primary_key=True, autoincrement=True)
    fk_date_id = Column(Integer, ForeignKey("dim_date.sk_date_id"))
    fk_exchange_id = Column(Integer, ForeignKey("dim_exchange.sk_exchange_id"))
    fk_commodity_id = Column(Integer, ForeignKey("dim_commodity.sk_commodity_id"))
    fk_index_id = Column(Integer, ForeignKey("dim_index.sk_index_id"))
    fk_stock_id = Column(Integer, ForeignKey("dim_stock.sk_stock_id"))
    symbol = Column(String)
    current_price = Column(Numeric)
    beta = Column(Numeric)
    market_cap = Column(Numeric)
    volume = Column(BigInteger)
    eps = Column(Numeric) # Pull net income (previous 4 quarters) and shares outstanding from income-statement API and divide net income/shares outstanding
    pe = Column(Numeric) # current_price / eps
    vwap = Column(Numeric)
    stock = relationship("DimStock", backref="market_metrics")
    date = relationship("DimDate", backref="market_metrics")
    exchange = relationship("DimExchange", backref="market_metrics")
    commodity = relationship("DimCommodity", backref="market_metrics")
    index = relationship("DimIndex", backref="market_metrics")



    def load_fact_market_metrics(session: Session, metrics_data: dict) -> int:
        """
            filters = [FactMarketMetrics.fk_date_id == metrics_data["fk_date_id"]]

            if metrics_data.get("fk_exchange_id") is not None:
                filters.append(FactMarketMetrics.fk_exchange_id == metrics_data["fk_exchange_id"])
            if metrics_data.get("fk_commodity_id") is not None:
                filters.append(FactMarketMetrics.fk_commodity_id == metrics_data["fk_commodity_id"])
            if metrics_data.get("fk_index_id") is not None:
                filters.append(FactMarketMetrics.fk_index_id == metrics_data["fk_index_id"])
            if metrics_data.get("fk_stock_id") is not None:
                filters.append(FactMarketMetrics.fk_stock_id == metrics_data["fk_stock_id"])

            # Query for existing record based on the filters
            existing = session.query(FactMarketMetrics).filter(*filters).one_or_none()
        

        if existing:
            # Return the primary key of the existing record
            return existing.sk_market_metrics_id
        """
        
        new_metric = FactMarketMetrics(
            fk_date_id=metrics_data.get("fk_date_id"),
            fk_exchange_id=metrics_data.get("fk_exchange_id"),
            fk_commodity_id=metrics_data.get("fk_commodity_id"),
            fk_index_id=metrics_data.get("fk_index_id"),
            fk_stock_id=metrics_data.get("fk_stock_id"),
            symbol=metrics_data.get("symbol"),
            current_price=metrics_data.get("current_price"),
            beta=metrics_data.get("beta"),
            market_cap=metrics_data.get("market_cap"),
            volume=metrics_data.get("volume"),
            eps=metrics_data.get("eps"),
            pe=metrics_data.get("pe"),
            vwap=metrics_data.get("vwap")
        )
        session.add(new_metric)
        session.commit()
        return new_metric.sk_market_metrics_id
        """
        Loads the fact market metrics data into the FactMarketMetrics instance.
        
        :param session: SQLAlchemy session object to query related tables.
        :param metrics_data: A dictionary containing the data to load.
        """
        # Assign basic attributes directly from the metrics_data
        self.symbol = metrics_data.get("symbol")
        self.current_price = metrics_data.get("current_price")
        self.market_cap = metrics_data.get("market_cap")
        self.volume = metrics_data.get("volume")
        self.eps = metrics_data.get("eps")
        self.pe = metrics_data.get("pe")
        self.vwap = metrics_data.get("vwap")

        # Load related tables (foreign keys) using session
        # For example, load the `DimDate`, `DimExchange`, etc., by matching the ids
        self.date = session.query(DimDate).filter(DimDate.sk_date_id == metrics_data["fk_date_id"]).one_or_none()
        self.exchange = session.query(DimExchange).filter(DimExchange.sk_exchange_id == metrics_data["fk_exchange_id"]).one_or_none()
        self.commodity = session.query(DimCommodity).filter(DimCommodity.sk_commodity_id == metrics_data["fk_commodity_id"]).one_or_none()
        self.index = session.query(DimIndex).filter(DimIndex.sk_index_id == metrics_data["fk_index_id"]).one_or_none()
        self.stock = session.query(DimStock).filter(DimStock.sk_stock_id == metrics_data["fk_stock_id"]).one_or_none()
