import dash
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import yfinance as yf
import plotly.graph_objs as go

from common.parse_query import make_list_from_string
#from pages.efficient_frontier.cards_efficient_frontier.ef_description import card_ef_description
from pages.explore_asset.cards.stock_info import card_ea_info
from pages.explore_asset.cards.ea_chart import card_graf
from pages.explore_asset.cards.controls import card_controls
# from pages.explore_asset.cards.ef_chart_transition_map import card_transition_map
from common.mobile_screens import adopt_small_screens
# from pages.efficient_frontier.prepare_ef_plot import prepare_transition_map, prepare_ef
import okama as ok

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
            # dbc.Row(
            #     html.Div(
            #         [
            #             dcc.Markdown(
            #                 """
            #             **Portfolio data**
            #             Click on points to get portfolio data.
            #             """
            #             ),
            #             html.P(id="ef-click-data-risk"),
            #             html.P(id="ef-click-data-return"),
            #             html.Pre(id="ef-click-data-weights"),
            #         ]
            #     ),
            # ),
            # dbc.Row(dbc.Col(card_transition_map, width=12), align="center"),
            # dbc.Row(dbc.Col(card_ef_description, width=12), align="left"),
        ],
        class_name="mt-2",
        fluid="md",
    )
    return page


@callback(
    Output(component_id="ea-graf", component_property="figure"),
    Output(component_id="ea-graf", component_property="config"),
    # Inputs
    Input(component_id="store", component_property="data"),
    # Main input for EF
    Input(component_id="ea-submit-button-state", component_property="n_clicks"),
    State(component_id="ea-symbols-list", component_property="value"),
    State(component_id="ea-start-date", component_property="value"),
    State(component_id="ea-end-date", component_property="value"),
    prevent_initial_call=False,
)
def update_ea_cards(screen, n_clicks, selected_symbols, sd_value, ed_value):
    # Ensure symbols is a list
    symbols = selected_symbols if isinstance(selected_symbols, list) else [selected_symbols]

    # Fetch stock data
    data = {symbol: yf.download(symbol, start=sd_value, end=ed_value) for symbol in symbols}

    # Plot
    traces = []
    for symbol, df in data.items():
        traces.append(go.Scatter(x=df.index, y=df['Close'], mode='lines', name=symbol))

    fig1 = {
        'data': traces,
        'layout': go.Layout(
            title='Stock Prices',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Price'}
        )
    }

    # Config for the graph
    config1 = {
        'displayModeBar': True,
        'displaylogo': False,
    }

    return fig1, config1


#
# @callback(
#     Output(component_id="ea-graf", component_property="figure"),
#     Output(component_id="ea-graf", component_property="config"),
#     # Inputs
#     Input(component_id="store", component_property="data"),
#     # Main input for EF
#     Input(component_id="ea-submit-button-state", component_property="n_clicks"),
#     State(component_id="ea-symbols-list", component_property="value"),
#     State(component_id="ea-start-date", component_property="value"),
#     State(component_id="ea-end-date", component_property="value"),
#     # # Options
#     # State(component_id="ef-plot-options", component_property="value"),
#     # State(component_id="cml-option", component_property="value"),
#     # State(component_id="risk-free-rate-option", component_property="value"),
#     # # Monte-Carlo
#     # State(component_id="monte-carlo-option", component_property="value"),
#     # # Transition Map
#     # State(component_id="transition-map-option", component_property="value"),
#     # # Input(component_id="ef-return-type-checklist-input", component_property="value"),
#     prevent_initial_call=False,
# )
# def update_ea_cards(
#         screen,
#         n_clicks,
#         # Main input
#         selected_symbols: list,
#         sd_value: str,
#         ed_value: str
#         # # Options
#         # plot_option: str,
#         # cml_option: str,
#         # rf_rate: float,
#         # n_monte_carlo: int,
#         # tr_map_option: str,
# ):
#     symbols = selected_symbols if isinstance(selected_symbols, list) else [selected_symbols]
#     ef_object = ok.EfficientFrontier(
#         symbols,
#         first_date=fd_value,
#         last_date=ld_value,
#         ccy=ccy,
#         inflation=False,
#         n_points=40,
#         full_frontier=True,
#     )
#     #ef_options = dict(plot_type=plot_option, cml=cml_option, rf_rate=rf_rate, n_monte_carlo=n_monte_carlo)
#     ef = ef_object.ef_points * 100
#     fig1 = prepare_ef(ef, ef_object, ef_options)
#     fig2 = prepare_transition_map(ef)
#
#     # Change layout for mobile screens
#     fig1, config1 = adopt_small_screens(fig1, screen)
#     fig2, config2 = adopt_small_screens(fig2, screen)
#
#     # Hide Transition map
#     transition_map_is_hidden = False if tr_map_option == "On" else True
#     return fig1, fig2, config1, config2, transition_map_is_hidden
