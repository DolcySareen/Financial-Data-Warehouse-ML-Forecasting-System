from app import db
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Boolean, DateTime\

class DimDate(db.Model):
    __tablename__ = 'dim_date'
    sk_date_id = Column(Integer, primary_key=True, autoincrement=True)
    full_date = Column(DateTime, nullable=False, unique=True)
    hour = Column(Integer)
    minute = Column(Integer)
    day_of_week = Column(Integer)
    day_name = Column(String(50))
    day_of_month = Column(Integer)
    day_of_year = Column(Integer)
    week_of_year = Column(Integer)
    month = Column(Integer)
    month_name = Column(String(50))
    quarter = Column(Integer)
    year = Column(Integer)
    fiscal_year = Column(Integer)
    is_weekend = Column(Boolean)
    am_pm = Column(String(2))
    def load_dim_date(session: Session, date_data: dict) -> int:
        # Check if the date already exists based on the full_date
        existing = session.query(DimDate).filter_by(full_date=date_data["full_date"]).one_or_none()

        if existing:
            # Update the existing record with new data
            for field, value in date_data.items():
                if hasattr(existing, field) and value is not None:
                    setattr(existing, field, value)

            session.commit()  # Save changes to the database
            return existing.sk_date_id

        # If the date does not exist, create a new record
        new_date = DimDate(
            full_date=date_data.get("full_date"),
            hour=date_data.get("hour"),
            minute=date_data.get("minute"),
            day_of_week=date_data.get("day_of_week"),
            day_name=date_data.get("day_name"),
            day_of_month=date_data.get("day_of_month"),
            day_of_year=date_data.get("day_of_year"),
            week_of_year=date_data.get("week_of_year"),
            month=date_data.get("month"),
            month_name=date_data.get("month_name"),
            quarter=date_data.get("quarter"),
            year=date_data.get("year"),
            fiscal_year=date_data.get("fiscal_year"),
            is_weekend=date_data.get("is_weekend"),
            am_pm=date_data.get("am_pm")
        )
        session.add(new_date)
        session.commit()  # Save the new record to the database
        return new_date.sk_date_id
