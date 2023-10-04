import dash_bootstrap_components as dbc
from dash import html, callback, dash_table, dcc
from dash.dependencies import Input, Output, State

ticker = State(component_id="ea-symbols-list", component_property="value")

# Placeholder graph cards
trailing_pe_graph = dbc.Card(
    dbc.CardBody(
        [
            html.H6(f"{ticker} price to Earnings (P/E)"),
            dbc.RadioItems(
                id="trailing-pe-time-range-radio",
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "3Y", "value": "3Y"},
                    {"label": "5Y", "value": "5Y"},
                    {"label": "All", "value": "ALL"},
                ],
                value="3Y",  # Default selected value
            ),
            dcc.Graph(id='trailing-pe-graph', figure={})  # Placeholder figure
        ]
    ),
    class_name="mb-3",
)

card_graph2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Graph 2"),
            dcc.Graph(id='graph-2', figure={})  # Placeholder figure
        ]
    ),
    class_name="mb-3",
)

card_graph3 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Graph 3"),
            dcc.Graph(id='graph-3', figure={})  # Placeholder figure
        ]
    ),
    class_name="mb-3",
)

card_graph4 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Graph 4"),
            dcc.Graph(id='graph-4', figure={})  # Placeholder figure
        ]
    ),
    class_name="mb-3",
)

card_valuation = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Valuation"),

            # First row of graphs
            dbc.Row([
                dbc.Col(trailing_pe_graph, width=6),  # Half the width (12/2)
                dbc.Col(card_graph2, width=6)
            ], className="mb-3"),  # margin-bottom to add some spacing between rows

            # Second row of graphs
            dbc.Row([
                dbc.Col(card_graph3, width=6),
                dbc.Col(card_graph4, width=6)
            ])
        ]
    ),
    class_name="mb-3",
)


def get_pe_graph(symbol: str, pe_time_range: str):
    """
    Get P/E graph for a given symbol.
    """
    


