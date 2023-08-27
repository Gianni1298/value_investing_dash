import re
from typing import Optional

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback
from dash.dependencies import Input, Output

import pandas as pd

from common import settings as settings #, inflation as inflation
# from common.create_link import create_link, check_if_list_empty_or_big
#from common.html_elements.copy_link_div import create_copy_link_div
from common.symbols import get_symbols
from common import cache
# import pages.efficient_frontier.cards_efficient_frontier.eng.ef_tooltips_options_txt as tl

app = dash.get_app()
cache.init_app(app.server)
options = get_symbols()

today_str = pd.Timestamp.today().strftime("%Y-%m-%d")


def card_controls(
        tickers: Optional[list],
        start_date: Optional[str],
        end_date: Optional[str],
        ccy: Optional[str],
):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H5("Explore Assets", className="card-title"),
                html.Div(
                    [
                        html.Label("Tickers to Explore"),
                        dcc.Dropdown(
                            options=options,
                            value=tickers if tickers else settings.default_symbols,
                            multi=False,
                            placeholder="Select assets",
                            id="ea-symbols-list",
                        ),
                    ],
                ),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Start Date"),
                                        dbc.Input(
                                            id="ea-start-date",
                                            value=start_date if start_date else "2000-01-01",
                                            type="text",
                                        ),
                                        dbc.FormText("Format: YYYY-MM-DD"),
                                    ],
                                ),
                                dbc.Col(
                                    [
                                        html.Label("End Date"),
                                        dbc.Input(
                                            id="ea-end-date",
                                            value=end_date if end_date else today_str,
                                            type="text",
                                        ),
                                        dbc.FormText("Format: YYYY-MM-DD"),
                                    ],
                                ),
                            ]
                        )
                    ]
                ),
                html.Div(
                    [
                        dbc.Button(
                            children="Update Graph",
                            id="ea-submit-button-state",
                            n_clicks=0,
                            color="primary",
                        ),
                    ],
                    style={"text-align": "center"},
                    className="p-3",
                ),
            ]
        ),
        class_name="mb-3",
    )
    return card

