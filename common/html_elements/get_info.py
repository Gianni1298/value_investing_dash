import yfinance as yf
import pandas as pd
from dash import dash_table
# import okama
from common.parse_query import get_marketCap


def get_info(assets: str) -> dash_table.DataTable:
    """
    Render DataTable with information about assets available historical period: length, first date, last date etc.
    """

    yf_ticker = [assets]
    info_list = []
    for ticker in yf_ticker:
        yf_ticker = yf.Ticker(ticker)
        long_name = yf_ticker.info.get("longName", "N/A")
        industry = yf_ticker.info.get("industry", "N/A")
        sector = yf_ticker.info.get("sector", "N/A")
        currency = yf_ticker.info.get("currency", "N/A")
        market_cap = get_marketCap(yf_ticker.info.get("marketCap", "N/A"))

        info_list += [
            {"Ticker": ticker, "Name": long_name, "Industry": industry, "Sector": sector, "Market Cap": market_cap, "Currency": currency}
        ]

    info_table = dash_table.DataTable(
        data=info_list,
        style_data={"whiteSpace": "normal", "height": "auto"},
    )
    return info_table
