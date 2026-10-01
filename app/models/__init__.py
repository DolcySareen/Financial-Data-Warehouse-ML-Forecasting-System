from .user import User
from .staging_minute_quote import StagingMinuteQuote
from .dim_date import DimDate
from .dim_index import DimIndex
from .dim_commodity import DimCommodity
from .dim_exchange import DimExchange
from .dim_stock import DimStock
from .dim_bond import DimBond
from .fact_market_metrics import FactMarketMetrics

# __all__ = [
#     "StagingMinuteQuote",
#     "DimCompany",
#     "DimDate",
#     "DimYield",
#     "DimIndex",
#     "DimCommodity",
#     "DimStock",
#     "DimBond",
#     "FactMarketMetrics",
# ]

# import inspect                                                              
# import pkgutil                                                                 
# import importlib                                                               
# import sys                                                                     


# def import_models():                                                           
#     thismodule = sys.modules[__name__]                                         

#     for loader, module_name, is_pkg in pkgutil.iter_modules(                   
#             thismodule.__path__, thismodule.__name__ + '.'):                   
#         module = importlib.import_module(module_name, loader.path)             
#         for name, _object in inspect.getmembers(module, inspect.isclass):      
#             globals()[name] = _object                                                                                     

# import_models() 