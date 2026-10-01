import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file.")

# Create the database engine
engine = create_engine(DATABASE_URL.format(os.getenv("POSTGRES_USER"), os.getenv("POSTGRES_PASSWORD")))

# Declare the Base
Base = declarative_base()

# Import your models here
# from app.models.fact_market_metrics import FactMarketMetrics
# from app.models.dim_stock import DimStock
# from app.models.dim_commodity import DimCommodity
# from app.models.dim_exchange import DimExchange
# from app.models.dim_bond import DimBond
# from app.models.dim_index import DimIndex
# from app.models.dim_date import DimDate
# from app.models.bond_market_metrics import BondMarketMetrics

# Create all tables
Base.metadata.create_all(engine)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def connect_to_database():
    try:
        # Connect to the database
        session = SessionLocal()
        print("✅ Successfully connected to the database!")
        return session
    except Exception as e:
        print(f"❌ Failed to connect to the database: {e}")
        return None


def main():
    connect_to_database()


if __name__ == "__main__":
    main()
