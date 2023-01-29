from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = Dash(external_stylesheets=[dbc.themes.CYBORG])
load_figure_template("CYBORG")

# add style for banner element
BANNER_STYLE = {
    "color": "white",
    "font-size": "4rem",
    "text-align": "center",
    "padding": "3rem",
    # add background image from local file
    "background-image": "url(https://lexica-serve-encoded-images2.sharif.workers.dev/full_jpg/7a303d4a-5e25-4c2d-b75b-52c3300668cf)",
    "background-size": "cover",
    "background-repeat": "no-repeat",
}

# update sidebar style to position it below the banner
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "4rem",  # adjust top position to be below the banner
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}

# update content style to position it below the banner and to the right of the sidebar
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-top": "4rem",  # adjust top position to be below the banner
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

banner = html.Div("DataSafari", style=BANNER_STYLE)

sidebar = html.Div(
    [
        html.H5("Menu"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Upload Data", href="/", active="exact"),
                dbc.NavLink("Explore Data", href="/page-2", active="exact"),
                dbc.NavLink("Statistics", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

df = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv"
)

fig = px.scatter(
    df,
    x="gdp per capita",
    y="life expectancy",
    size="population",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)


app.layout = html.Div(
    [
        banner,  # add the banner element
        # App Header in center
        dbc.Row(
            [
                dbc.Col(html.Div([sidebar]), width=2),
                dbc.Col(
                    html.Div(
                        [
                            dcc.Graph(
                                id="life-exp-vs-gdp",
                                figure=fig,
                            ),
                        ]
                    ),
                    width=8,
                ),
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="my-output", component_property="children"),
    Input(component_id="my-input", component_property="value"),
)
def update_output_div(input_value):
    return f"Output: {input_value}"


if __name__ == "__main__":
    app.run_server(debug=True)
