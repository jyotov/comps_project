import dash
from dash import Dash, html, dcc, callback, Output, Input, State

app = Dash(__name__, use_pages=True)

# other components from https://dash.plotly.com/dash-core-components/input
# doc: https://docs.google.com/document/d/1xv4Elh_HFrELS-goC2hW1_Nv90O_R3M-T3Inai_4N0A/edit

app.layout = html.Div([
    html.H1(children='Testing Tutorial: Python', style={'textAlign': 'center'}),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

# def layout_home():
#     return html.Div([
#         html.H2("Home Page"),
#         html.P("Welcome to the home page!"),
#         dcc.Link("Go to Category 1", href="/category1", style={"margin-right": "15px"}),
#         dcc.Link("Go to Category 2", href="/category2"),
#     ])
#
# def layout_category1():
#     return html.Div([
#         html.H2("Category 1"),
#         html.P("This is the Category 1 main page."),
#         dcc.Link("Go to Subpage 1", href="/category1/subpage", style={"margin-right": "15px"}),
#         dcc.Link("Go back to Home", href="/")
#     ])
#
# def layout_category1_subpage():
#     return html.Div([
#         html.H2("Category 1 > Subpage"),
#         html.P("This is a subpage under Category 1."),
#         dcc.Link("Go back to Category 1", href="/category1", style={"margin-right": "15px"}),
#         dcc.Link("Go back to Home", href="/"),
#     ])
#
# def layout_category2():
#     return html.Div([
#         html.H2("Category 2"),
#         html.P("This is the Category 2 main page."),
#         dcc.Link("Go back to Home", href="/"),
#     ])
#
# # Main layout with navigation
# app.layout = html.Div([
#     html.Header([
#         html.H1("Multi-Page Dash App", style={"text-align": "center"}),
#     ]),
#     html.Nav([
#         dcc.Link("Home", href="/", style={"margin-right": "15px"}),
#         dcc.Link("Category 1", href="/category1", style={"margin-right": "15px"}),
#         dcc.Link("Category 2", href="/category2"),
#     ], style={"text-align": "center", "margin-bottom": "20px"}),
#     html.Div(id="page-content", style={"padding": "20px"}),
#     dcc.Location(id="url", refresh=False),
# ])
#
# # Callback to dynamically load pages
# @app.callback(
#     Output("page-content", "children"),
#     Input("url", "pathname")
# )
# def display_page(pathname):
#     if pathname == "/category1/subpage":
#         return layout_category1_subpage()
#     elif pathname == "/category1":
#         return layout_category1()
#     elif pathname == "/category2":
#         return layout_category2()
#     else:
#         return layout_home()


if __name__ == '__main__':
    app.run(debug=True)

# exec is not the most secure -> address in ethical considerations
# code coverage -> does it trigger all of the lines to run -> for edge cases