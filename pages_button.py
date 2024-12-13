import dash
from dash import dcc, html, Input, Output

# Import layout objects from subpages
from pages.add import layout as add_layout
from pages.count import layout as count_layout

# Mapping subpages to their layout objects
SUBPAGE_LAYOUTS = {
    "Warmup Exercises": {
        "add": add_layout
    },
    "String Exercises": {

    },
    "List Exercises": {

    },
    "For Loop Exercises": {
        "count": count_layout
    },
    "While Loop Exercises": {

    },
    "Nested Loop Exercises": {

    },
}

# Define categories and their subpages
CATEGORIES = {
    "Warmup Exercises": ["add"],
    "String Exercises": [""],
    "List Exercises": [""],
    "For Loop Exercises": ["count"],
    "While Loop Exercises": [""],
    "Nested Loop Exercises": [""]
}

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='navigation', children=[
        html.H1(children='Testing Tutorial', style={'textAlign': 'center'}),
        html.Div('This resource is designed to provide students in introductory level computer science classes with '
                 'extra practice with defining and testing functions. Click on any category below to view all of the corresponding exercises. '
                 'Each exercise will ask you to define a function in Python and write some unit tests to test your code.',
                 style={"margin-bottom": "10px"}),
        html.Div([
            html.Button(category, id=f"{category}-button", n_clicks=0, style={"margin-right": "10px"})
            for category in CATEGORIES.keys()
        ]),
        html.Button("Return to Home", id="home-button", n_clicks=0, style={"margin-top": "10px"}),
    ]),
    html.Div(id='category-content'),  # Displays the list of subpages for a category
    html.Div(id='page-content')  # Displays the content of a selected subpage
])

# Unified callback to manage both category and page content
@app.callback(
    [Output('category-content', 'children'),
     Output('page-content', 'children')],
    [Input('url', 'pathname')] +
    [Input(f"{category}-button", 'n_clicks') for category in CATEGORIES.keys()] +
    [Input('home-button', 'n_clicks')]
)
def update_content(pathname, *args):
    ctx = dash.callback_context

    # Handle button clicks (categories or home button)
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        # Handle the "Return to Home" button
        if button_id == 'home-button':
            return html.P("Click a category to view subpages."), None

        # Handle category buttons
        for category in CATEGORIES.keys():
            if button_id == f"{category}-button":
                return html.Div([
                    html.H2(f"{category}"),
                    html.Ul([
                        html.Li(dcc.Link(subpage, href=f"/{category}/{subpage}"))
                        for subpage in CATEGORIES[category]
                    ])
                ]), None

    # Handle URL changes (subpage navigation)
    if pathname and pathname != '/':
        path_parts = pathname.strip('/').split('/')
        if len(path_parts) == 2:
            category, subpage = path_parts
            category = category.replace('%20', ' ')  # Handle spaces in category names

            if category in SUBPAGE_LAYOUTS and subpage in SUBPAGE_LAYOUTS[category]:
                return None, html.Div(SUBPAGE_LAYOUTS[category][subpage])

    # Default to home page message
    return html.P("Click a category to view subpages."), None

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)






