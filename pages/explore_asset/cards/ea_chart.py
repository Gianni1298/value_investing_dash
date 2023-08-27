from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
import yfinance as yf
import plotly.graph_objs as go

card_graf = dbc.Card(
    dbc.CardBody([html.Div(dcc.Loading(dcc.Graph(id="ea-graf")))]),
    class_name="mb-3",
)


def get_stock_graph(symbol, sd_value, ed_value):
    # Fetch stock data
    data = {symbol: yf.download(symbol, start=sd_value, end=ed_value) for symbol in symbol}

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