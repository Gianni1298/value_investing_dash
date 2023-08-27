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
                # html.Div(
                #     [
                #         html.Label("Base currency"),
                #         dcc.Dropdown(
                #             options=get_currency_list(),
                #             value=ccy if ccy else "USD",
                #             multi=False,
                #             placeholder="Select a base currency",
                #             id="ea-base-currency",
                #         ),
                #     ],
                # ),
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
                            children="Submit",
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

#
# @app.callback(
#     Output("ea-symbols-list", "options"),
#     Input("ea-symbols-list", "search_value"),
#     Input("ea-symbols-list", "value"),
# )
# def optimize_search_ef(search_value, selected_values):
#     return (
#         [o for o in options if re.match(search_value, o, re.IGNORECASE) or o in (selected_values or [])]
#         if search_value
#         else selected_values
#     )

#
# @app.callback(
#     Output("ea-symbols-list", "disabled"),
#     Input("ea-symbols-list", "value"),
# )
# def disable_search(tickers_list) -> bool:
#     """
#     Disable asset search form if the number of ticker exceeds allowed in settings.
#     """
#     return len(tickers_list) >= settings.ALLOWED_NUMBER_OF_TICKERS


# @app.callback(
#     Output("ea-submit-button-state", "disabled"),
#     Input("ea-symbols-list", "value"),
# )
# def disable_submit(tickers_list) -> bool:
#     """
#     Disable Submit button.
#
#     conditions:
#     - number of tickers is < 2
#     - MC number is incorrect
#     """
#     return len(tickers_list) > 1