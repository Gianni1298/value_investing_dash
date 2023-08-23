import dash_bootstrap_components as dbc
from dash import html, callback, dash_table
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import yfinance as yf
import okama as ok

from common.html_elements.get_info import get_assets_names, get_info

card_ea_info = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Information"),
            html.Div(id="info"),
            html.H5("Assets names"),
            html.Div(id="ea-assets-names"),
        ]
    ),
    class_name="mb-3",
)


@callback(
    Output("ea-assets-names", "children"),
    Output("info", "children"),
    Input("ea-symbols-list", "value"),  # tickers
    prevent_initial_call=False,
)
def pf_update_asset_names_info(assets: list) -> dash_table.DataTable:
    assets = [i for i in assets if i is not None]
    if not assets:
        raise PreventUpdate
    # al_object = ok.AssetList(assets)
    # names_table = get_assets_names(al_object)
    info_table = get_info(assets)
    return names_table, info_table
