import dash
from dash import html, dcc, callback, Output, Input, State

dash.register_page(__name__)

layout = html.Div([
    html.H1(children='Home'),
    html.Div('Select one of the categories below to see all relevant exercises.'),
    # dcc.Location(id='url', refresh=False),  # Keeps track of the URL
    # html.Div([
    #     # html.Button("Go to Home", id="home-button", n_clicks=0),
    #     html.Button("Warmup Exercises", id="warmup", n_clicks=0),
    #     html.Button("String Exercises", id="strings", n_clicks=0),
    #     html.Button("List Exercises", id="lists", n_clicks=0),
    # ]),
])

# @callback(
#     Output('url', 'pathname'),
#     [Input('warmup', 'n_clicks'),
#      Input('strings', 'n_clicks'),
#      Input('lists', 'n_clicks')]
# )
# def navigate(home_clicks, page1_clicks, page2_clicks):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return '/'
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     if button_id == 'warmup':
#         return '/'
#     elif button_id == 'stings':
#         return '/page-1'
#     elif button_id == 'lists':
#         return '/page-2'
#     return '/'

