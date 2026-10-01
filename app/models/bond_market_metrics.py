from app import db
from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship

class BondMarketMetrics(db.Model):
    __tablename__ = "bond_market_metrics"

    sk_market_metrics_id = Column(Integer, primary_key=True, autoincrement=True)
    fk_bond_id = Column(Integer, ForeignKey("dim_bond.sk_bond_id"))
    fk_date_id = Column(Integer, ForeignKey("dim_date.sk_date_id"))
    m1_month = Column(Numeric)
    m2_month = Column(Numeric)
    m3_month = Column(Numeric)
    m6_month = Column(Numeric)
    m1_year = Column(Numeric)
    m2_year = Column(Numeric)
    m3_year = Column(Numeric)
    m5_year = Column(Numeric)
    m7_year = Column(Numeric)
    m10_year = Column(Numeric)
    m20_year = Column(Numeric)
    m30_year = Column(Numeric)

    bond = relationship("DimBond", backref="bond_market_metrics")
    date = relationship("DimDate", backref="bond_market_metrics")

    @staticmethod
    def load_bond_market_metrics(session, metrics_data):
        new_metrics = BondMarketMetrics(
            fk_bond_id=metrics_data.get("fk_bond_id"),
            fk_date_id=metrics_data.get("fk_date_id"),
            m1_month=metrics_data.get("m1_month"),
            m2_month=metrics_data.get("m2_month"),
            m3_month=metrics_data.get("m3_month"),
            m6_month=metrics_data.get("m6_month"),
            m1_year=metrics_data.get("m1_year"),
            m2_year=metrics_data.get("m2_year"),
            m3_year=metrics_data.get("m3_year"),
            m5_year=metrics_data.get("m5_year"),
            m7_year=metrics_data.get("m7_year"),
            m10_year=metrics_data.get("m10_year"),
            m20_year=metrics_data.get("m20_year"),
            m30_year=metrics_data.get("m30_year")
        )
        session.add(new_metrics)
        session.commit()
        return new_metrics.sk_market_metrics_id