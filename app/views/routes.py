import os
import pandas as pd
import plotly.express as px
from app import db
from app.models import *
from app.models.user import User
from app.models.fact_market_metrics import FactMarketMetrics
from app.views.forms import LoginForm, ParametersForm, RegistrationForm
from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.controllers.main_controller import execute_stock_data, execute_exchange_data, execute_commodity_data, execute_index_data, execute_bond_data, execute_fact_hourly, execute_bond_metrics
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def landing():
    return redirect(url_for('main.portal'))

@main.route('/portal')
def portal():
    return render_template('portal.html', title='Algotrading Portal')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login unsuccessful.<br/>Please check your email and password.', 'danger')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data)
            new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!<br/>You can now log in.', 'success')
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
    return render_template('register.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.portal'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard', dashboard_state='active')

@main.route('/visualization', methods=['GET', 'POST'])
@login_required
def visualization():
    try:
        asset_types = ['stock', 'commodity', 'exchange', 'index','bonds']
        selected_type = request.form.get('asset_type', 'stock')

        # Fetch symbols based on the selected asset type
        if selected_type == 'stock':
            symbols = db.session.query(DimStock.symbol).distinct().all()
        elif selected_type == 'commodity':
            symbols = db.session.query(DimCommodity.symbol).distinct().all()
        elif selected_type == 'exchange':
            symbols = db.session.query(DimExchange.symbol).distinct().all()
        elif selected_type == 'index':
            symbols = db.session.query(DimIndex.symbol).distinct().all()
        elif selected_type == 'bonds':
            symbols = db.session.query(DimBond.treasury_name).distinct().all()
        else:
            symbols = []

        stock_symbols = [symbol[0] for symbol in symbols]  # Extract symbols from query result

        # Get the selected symbol from the form or default to the first symbol
        selected_symbol = request.form.get('stock_symbol') if request.method == 'POST' else stock_symbols[0]

        # Get the selected time frame
        today = datetime.today().strftime('%Y-%m-%d')
        start_date = request.form.get('start_date', '2020-01-01')
        end_date = request.form.get('end_date', today)
        
        # Parse the dates as datetime objects
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Get the selected plot lines
        show_volume = 'show_volume' in request.form
        show_price = 'show_price' in request.form
        show_market_cap = 'show_market_cap' in request.form
        show_eps = 'show_eps' in request.form
        show_pe = 'show_pe' in request.form
        show_vwap = 'show_vwap' in request.form

        # Fetch data for the selected symbol and time frame
        data = db.session.query(FactMarketMetrics).filter(
            FactMarketMetrics.symbol == selected_symbol
        ).all()

        # Create a DataFrame from the fetched data
        df = pd.DataFrame([{
            'Date': d.date.full_date,
            'Current Price': d.current_price,
            'Volume': d.volume,
            'Market Cap': d.market_cap,
            'EPS': d.eps,
            'PE': d.pe,
            'VWAP': d.vwap
        } for d in data])

        # Generate a Plotly graph
        fig = px.line(data_frame=df.sort_values(by='Date'), x='Date', y='Current Price', title=f'{selected_type.capitalize()} Prices for {selected_symbol}', log_y=True)

        if show_volume:
            fig.add_scatter(x=df['Date'], y=df['Volume'], mode='lines', name='Volume')
        if show_price:
            fig.add_scatter(x=df['Date'], y=df['Current Price'], mode='lines', name='Price')
        if show_market_cap:
            fig.add_scatter(x=df['Date'], y=df['Market Cap'], mode='lines', name='Market Cap')
        if show_eps:
            fig.add_scatter(x=df['Date'], y=df['EPS'], mode='lines', name='EPS')
        if show_pe:
            fig.add_scatter(x=df['Date'], y=df['PE'], mode='lines', name='PE')
        if show_vwap:
            fig.add_scatter(x=df['Date'], y=df['VWAP'], mode='lines', name='VWAP')

        graph_html = fig.to_html(full_html=False)

        return render_template('dashboard.html', title='Visualization', visualization_state = 'active', asset_types=asset_types, selected_type=selected_type, stock_symbols=stock_symbols, selected_symbol=selected_symbol, start_date=start_date, end_date=end_date, show_volume=show_volume, show_price=show_price, show_market_cap=show_market_cap, show_eps=show_eps, show_pe=show_pe, show_vwap=show_vwap, graph_html=graph_html)
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
        return redirect(url_for('main.dashboard'))

# def visualization():
#     try:
#         # Fetch distinct stock symbols from the database
#         stock_symbols = db.session.query(FactMarketMetrics.symbol).distinct().all()
#         stock_symbols = [symbol[0] for symbol in stock_symbols]  # Extract symbols from query result

#         # Get the selected symbol from the form or default to the first symbol
#         selected_symbol = request.form.get('stock_symbol') if request.method == 'POST' else stock_symbols[0]

#         # Debug: Print the selected symbol
#         print(f"Selected Symbol: {selected_symbol}")

#         # Fetch data for the selected symbol
#         data = db.session.query(FactMarketMetrics).filter_by(symbol=selected_symbol).all()

#         # Create a DataFrame from the fetched data
#         df = pd.DataFrame([{
#             'Date': d.date.full_date,
#             'Current Price': d.current_price,
#             'Volume': d.volume
#         } for d in data])

#         # Generate a Plotly graph
#         fig = px.line(data_frame=df.sort_values(by='Date'), x='Date', y='Current Price', title=f'Stock Prices for {selected_symbol}', log_y=True)
#         graph_html = fig.to_html(full_html=False)

#         return render_template('dashboard.html', title='Visualization', visualization_state='active', stock_symbols=stock_symbols, selected_symbol=selected_symbol, graph_html=graph_html)
#     except Exception as e:
#         flash(f'An error occurred: {str(e)}', 'danger')
#         return redirect(url_for('main.dashboard'))

@main.route('/general-settings')
@login_required
def general_settings():
    return render_template('dashboard.html', title='General Settings', general_settings_state='active')

@main.route('/trading-parameters')
@login_required
def trading_parameters():
    return render_template('dashboard.html', title='Trading Parameters', trading_parameters_state='active')

@main.route('/ml-models')
@login_required
def ml_models():
    return render_template('dashboard.html', title='ML Models', ml_models_state='active')

@main.route('/data-settings')
@login_required
def data_settings():
    return render_template('dashboard.html', title='Data Settings', data_settings_state='active')

@main.route('/visualization-settings')
@login_required
def visualization_settings():
    return render_template('dashboard.html', title='Visualization Settings', visualization_settings_state='active')

# Data Management Routes
@main.route('/get_symbols')
@login_required
def get_symbols():
    asset_type = request.args.get('asset_type', 'stock')
    if asset_type == 'stock':
        symbols = db.session.query(DimStock.symbol).distinct().all()
    elif asset_type == 'commodity':
        symbols = db.session.query(DimCommodity.symbol).distinct().all()
    elif asset_type == 'exchange':
        symbols = db.session.query(DimExchange.symbol).distinct().all()
    elif asset_type == 'index':
        symbols = db.session.query(DimIndex.symbol).distinct().all()
    else:
        symbols = []

    symbols = [symbol[0] for symbol in symbols]  # Extract symbols from query result
    return jsonify({'symbols': symbols})

# Data Execution Routes
@main.route('/execute_stock_data')
@login_required
def execute_stock_data_route():
    try:
        execute_stock_data()
        flash('Stock data executed successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('main.data_settings'))

@main.route('/execute_exchange_data')
@login_required
def execute_exchange_data_route():
    try:
        execute_exchange_data()
        flash('Exchange data executed successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('main.data_settings'))

@main.route('/execute_commodity_data')
@login_required
def execute_commodity_data_route():
    try:
        execute_commodity_data()
        flash('Commodity data executed successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('main.data_settings'))

@main.route('/execute_index_data')
@login_required
def execute_index_data_route():
    try:
        execute_index_data()
        flash('Index data executed successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('main.data_settings'))

@main.route('/execute_bond_data')
@login_required
def execute_bond_data_route():
    try:
        execute_bond_data()
        flash('Bond data executed successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('main.data_settings'))

@main.route('/execute_fact_hourly')
@login_required
def execute_fact_hourly_route():
    try:
        execute_fact_hourly()
        flash('Fact hourly data executed successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('main.data_settings'))

@main.route('/execute_bond_metrics')
@login_required
def execute_bond_metrics_route():
    try:
        execute_bond_metrics()
        flash('Bond metrics executed successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('main.data_settings'))
