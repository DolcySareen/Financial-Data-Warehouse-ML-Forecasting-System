from app import db
from app.models import DimExchange, DimStock, DimDate, DimBond, DimIndex, DimCommodity, FactMarketMetrics, FactBondMetrics

class Loader:

    @staticmethod
    def load_exchange_data(transformed_data):
        """
        Load transformed exchange data into the DimExchange table.
        :param transformed_data: Dictionary containing transformed exchange data.
        """
        exchange = DimExchange(**transformed_data)
        db.session.add(exchange)
        db.session.commit()

    @staticmethod
    def load_stock_data(transformed_data):
        """
        Load transformed stock data into the DimStock table.
        :param transformed_data: Dictionary containing transformed stock data.
        """
        stock = DimStock(**transformed_data)
        db.session.add(stock)
        db.session.commit()

    @staticmethod
    def load_date_data(transformed_data):
        """
        Load transformed date data into the DimDate table.
        :param transformed_data: Dictionary containing transformed date data.
        """
        date = DimDate(**transformed_data)
        db.session.add(date)
        db.session.commit()

    @staticmethod
    def load_bond_data(transformed_data):
        """
        Load transformed bond data into the DimBond table.
        :param transformed_data: Dictionary containing transformed bond data.
        """
        bond = DimBond(**transformed_data)
        db.session.add(bond)
        db.session.commit()

    @staticmethod
    def load_index_data(transformed_data):
        """
        Load transformed index data into the DimIndex table.
        :param transformed_data: Dictionary containing transformed index data.
        """
        index = DimIndex(**transformed_data)
        db.session.add(index)
        db.session.commit()

    @staticmethod
    def load_commodity_data(transformed_data):
        """
        Load transformed commodity data into the DimCommodity table.
        :param transformed_data: Dictionary containing transformed commodity data.
        """
        commodity = DimCommodity(**transformed_data)
        db.session.add(commodity)
        db.session.commit()

    @staticmethod
    def load_fact_data(transformed_data):
        """
        Load transformed fact data into the FactMarketMetrics table.
        :param transformed_data: Dictionary containing transformed fact data.
        """
        fact = FactMarketMetrics(**transformed_data)
        db.session.add(fact)
        db.session.commit()

    @staticmethod
    def load_bond_metrics_data(transformed_data):
        """
        Load transformed bond metrics data into the FactBondMetrics table.
        :param transformed_data: Dictionary containing transformed bond metrics data.
        """
        bond_metrics = FactBondMetrics(**transformed_data)
        db.session.add(bond_metrics)
        db.session.commit()