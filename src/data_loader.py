import yfinance as yf
import pandas as pd

def load_price_data(ticker, start="2010-01-01", end="2024-12-31", auto_adjust=True):
    """
    Descarga precios históricos de Yahoo Finance y limpia columnas.
    """
    data = yf.download(ticker, start=start, end=end, auto_adjust=auto_adjust)

    # Flatten MultiIndex if exists
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Selecciona precio de cierre
    if 'Close' in data.columns:
        data = data[['Close']]
        data.rename(columns={'Close':'price'}, inplace=True)
    elif 'Adj Close' in data.columns:
        data = data[['Adj Close']]
        data.rename(columns={'Adj Close':'price'}, inplace=True)

    return data
