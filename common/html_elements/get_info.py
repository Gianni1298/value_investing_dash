import yfinance as yf
import pandas as pd
from dash import dash_table
import okama
from common.parse_query import get_marketCap


def get_assets_names(al_object: okama.AssetList) -> dash_table.DataTable:
    """
    Render DataTable with assets names.
    """
    names_df = (
        pd.DataFrame.from_dict(al_object.names, orient="index")
        .reset_index(drop=False)
        .rename(columns={"index": "Ticker", 0: "Name"})[["Ticker", "Name"]]
    )
    return dash_table.DataTable(
        data=names_df.to_dict(orient="records"),
        style_data={
            "whiteSpace": "normal",
            "height": "auto",
        },
        # page_size=4,
    )


def get_info(assets: list) -> dash_table.DataTable:
    """
    Render DataTable with information about assets available historical period: length, first date, last date etc.
    """
    yf_tickers = [asset.split('.')[0] for asset in assets]

    info_list = []
    for ticker in yf_tickers:
        yf_ticker = yf.Ticker(ticker)
        long_name = yf_ticker.info.get("longName", "N/A")
        industry = yf_ticker.info.get("industry", "N/A")
        sector = yf_ticker.info.get("sector", "N/A")
        marketCap = get_marketCap(yf_ticker.info.get("marketCap", "N/A"))

        info_list += [
            {"Ticker": ticker, "Name": long_name, "Industry": industry, "Sector": sector, "Market Cap": marketCap}
        ]

    info_table = dash_table.DataTable(
        data=info_list,
        style_data={"whiteSpace": "normal", "height": "auto"},
    )
    return info_table
