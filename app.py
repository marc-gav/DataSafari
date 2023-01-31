from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

from html_components.components import (
    sidebar,
    banner,
    introduction,
    description,
    content,
)

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.FONT_AWESOME],
)


app.layout = html.Div(
    [
        banner,
        introduction,
        description,
        dcc.Location(id="url"),
        dbc.Row(
            [
                dbc.Col(html.Div([sidebar]), width=2),
                dbc.Col(html.Div([content]), width=10),
            ],
            align="center",
        ),
        dcc.Interval(id="interval-component", interval=200, n_intervals=0),
        html.Img(
            id="animated-rocket",
            src=app.get_asset_url("cute_astro.svg"),
            className="rocket-animation",
        ),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-2":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(debug=True)
