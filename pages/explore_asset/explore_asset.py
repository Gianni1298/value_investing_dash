import dash
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import yfinance as yf
import plotly.graph_objs as go

from common.parse_query import make_list_from_string
from pages.explore_asset.cards.stock_info import card_ea_info
from pages.explore_asset.cards.ea_chart import card_graf, get_stock_graph
from pages.explore_asset.cards.controls import card_controls
from pages.explore_asset.cards.valuation import card_valuation, get_pe_graph


dash.register_page(
    __name__,
    path="/",
    title="Explore Stock",
    name="Explore Stock",
    description="Explore Stock application to compare assets.",
)


def layout(tickers=None, start_date=None, end_date=None, ccy=None, **kwargs):
    tickers_list = make_list_from_string(tickers)
    page = dbc.Container(
        [
            dbc.Row(card_controls(tickers_list, start_date, end_date, ccy), align="center"),
            dbc.Row(card_ea_info, align="center"),
            dbc.Row(dbc.Col(card_graf, width=12), align="center"),
            dbc.Row(dbc.Col(card_valuation, width=12), align="center"),
        ],
        class_name="mt-2",
        fluid="md",
    )
    return page


@callback(
    Output(component_id="ea-graf", component_property="figure"),
    Output(component_id="ea-graf", component_property="config"),
    Output(component_id="trailing-pe-graph", component_property="figure"),
    # Inputs
    Input(component_id="store", component_property="data"),
    # Main input for EA
    Input(component_id="ea-submit-button-state", component_property="n_clicks"),
    State(component_id="ea-symbols-list", component_property="value"),
    State(component_id="ea-start-date", component_property="value"),
    State(component_id="ea-end-date", component_property="value"),
    State(component_id="trailing-pe-time-range-radio", component_property="value"),
    prevent_initial_call=False,
)
def update_ea_cards(screen, n_clicks, selected_symbols, sd_value, ed_value, pe_time_range):
    # Ensure symbols is a list
    symbol = selected_symbols if isinstance(selected_symbols, list) else [selected_symbols]

    # stock graph
    fig1, config1 = get_stock_graph(symbol, sd_value, ed_value)

    # P/E graph
    fig2 = get_pe_graph(symbol, pe_time_range)

    return fig1, config1

