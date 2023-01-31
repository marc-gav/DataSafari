from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

banner = html.Div(children=[html.H1("Data Voyager", className="banner-style")])
introduction = html.Div(
    "Embark on an Odyssey with Data Voyager!",
    className="content-style",
)
description = html.Div(
    "Explore the universe of your machine learning datasets with ease. Upload your data and watch as it comes to life with insightful visualizations, outlier detection, and class imbalance analysis. Correct any anomalies you encounter along the way, and discover hidden insights with the power of Data Voyager. Launch your data journey now!",
    className="content-style2",
)
sidebar = html.Div(
    [
        dbc.Row(
            children=[
                dbc.Col("MENU", style={"textAlign": "center"}, width=12),
            ]
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    href="/",
                    active="exact",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Span(
                                        className="fa fa-light fa-home",
                                        style={"marginRight": "10px"},
                                    ),
                                ),
                                dbc.Col("Home"),
                            ]
                        ),
                    ],
                ),
                dbc.NavLink(
                    href="/page-2",
                    active="exact",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Span(
                                        className="fa fa-light fa-upload",
                                        style={"marginRight": "10px"},
                                    ),
                                ),
                                dbc.Col("Upload"),
                            ]
                        ),
                    ],
                ),
                dbc.NavLink(
                    href="/page-3",
                    active="exact",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Span(
                                        className="fa fa-light fa-rocket",
                                        style={"marginRight": "10px"},
                                    ),
                                ),
                                dbc.Col("Explore"),
                            ]
                        ),
                    ],
                ),
                dbc.NavLink(
                    href="/page-4",
                    active="exact",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Span(
                                        className="fa fa-light fa-bar-chart",
                                        style={"marginRight": "10px"},
                                    ),
                                ),
                                dbc.Col("Statistics"),
                            ]
                        ),
                    ],
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar-style",
)
content = html.Div(id="page-content", className="content-style")
