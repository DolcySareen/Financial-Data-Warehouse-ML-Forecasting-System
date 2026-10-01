import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
#csrf = CSRFProtect()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    # Load secret key from .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    # Load database URL from .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    #csrf.init_app(app)

    login_manager.login_view = 'main.login'

    # Create tables
    with app.app_context():
        db.create_all()

    # Import and register blueprints
    from app.views.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

from app.models.bond_market_metrics import BondMarketMetrics
from app.models.dim_bond import DimBond
from app.models.dim_commodity import DimCommodity
from app.models.dim_date import DimDate
from app.models.dim_exchange import DimExchange
from app.models.dim_index import DimIndex
from app.models.dim_stock import DimStock
from app.models.fact_market_metrics import FactMarketMetrics
from app.models.staging_minute_quote import StagingMinuteQuote
from app.models.user import User

# Define the user_loader callback
@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))