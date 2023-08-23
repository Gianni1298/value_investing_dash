import dash
from dash import html, dcc


def footer():
    return html.Footer(
        html.Div(
            [
                html.Hr(),
                dcc.Markdown(
                    """
                **Value-investment** open source free project. *MIT License*  
                """
                ),
                html.P(
                    [
                        html.Img(src=dash.get_asset_url("GitHub-Mark-32px.png")),
                        html.Span("   "),
                        html.A("GitHub Repository", href="https://github.com/Gianni1298/value_investing_dash", target="_blank"),
                    ]
                ),
            ],
            style={"text-align": "center"},
            className="p-3",
        ),
    )