import dash
from dash import dcc, html, Input, Output

# Imports warmup subpages
from pages.add import layout as add_layout
from pages.even_odd import layout as even_odd_layout
from pages.days_in_month import layout as days_in_month_layout

# Imports string subpages
from pages.first_last import layout as first_last_layout
from pages.reverse import layout as reverse_layout
from pages.repeat_first import layout as repeat_first_layout

# Imports list subpages
from pages.equal_first_last import layout as equal_first_last_layout
from pages.middle_values import layout as middle_values_layout
from pages.rotate_right import layout as rotate_right_layout

# Imports for loop subpages
from pages.count import layout as count_layout
from pages.triple_chars import layout as triple_chars_layout
from pages.draw_star_triangle import layout as draw_star_triangle_layout

# Imports for while loop subpages
from pages.five_mults import layout as five_mults_layout
from pages.in_half import layout as in_half_layout
from pages.sum import layout as sum_layout

SUBPAGE_LAYOUTS = {
    "Warmup Exercises": {
        "add": add_layout,
        "even_odd": even_odd_layout,
        "days_in_month": days_in_month_layout,
    },
    "String Exercises": {
        "first_last": first_last_layout,
        "reverse": reverse_layout,
        "repeat_first": repeat_first_layout,
    },
    "List Exercises": {
        "equal_first_last": equal_first_last_layout,
        "middle_values": middle_values_layout,
        "rotate_right": rotate_right_layout,
    },
    "For Loop Exercises": {
        "count": count_layout,
        "triple_chars": triple_chars_layout,
        "draw_star_triangle": draw_star_triangle_layout,
    },
    "While Loop Exercises": {
        "five_mults": five_mults_layout,
        "in_half": in_half_layout,
        "sum": sum_layout,
    },
}

CATEGORIES = {
    "Warmup Exercises": ["add", "even_odd", "days_in_month"],
    "String Exercises": ["first_last", "reverse", "repeat_first"],
    "List Exercises": ["equal_first_last", "middle_values", "rotate_right"],
    "For Loop Exercises": ["count", "triple_chars", "draw_star_triangle"],
    "While Loop Exercises": ["five_mults", "in_half", "sum"],
}

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# App layout
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

@app.callback(
    [Output('category-content', 'children'),
     Output('page-content', 'children')],
    [Input('url', 'pathname')] +
    [Input(f"{category}-button", 'n_clicks') for category in CATEGORIES.keys()] +
    [Input('home-button', 'n_clicks')]
)
def update_content(pathname, *args):
    ctx = dash.callback_context

    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'home-button':
            return html.P("As the name suggests, unit tests allow you to test your code in isolated small 'units', "
                            "rather than having to test an entire application. In these exercises, the 'unit' to be "
                            "tested is a function that you first need to define. However, it may be helpful to note "
                            "some test cases and their expected outputs before actually writing the function. All "
                            "test cases can be written directly into the grid below each function. Be sure to fill in "
                            "all of the rows with test cases. The number of rows for each table varies for different "
                            "functions. A function with two boolean arguments (True and False) will only have four possible "
                            "test cases (where the arguments are True and True, True and False, False and True, and False and False). "
                            "However, other functions (for example, one with two integer arguments) has an infinite number of "
                            "possible test cases. Therefore, you will need to think of test cases that adequeately test your function. "
                            "This often means considering edge cases. If a function has an argument that is a string, an important "
                            "edge case is an empty string. Similarly, if a function has an argument that is a list, an important "
                            "edge case is an empty list. For functions with integer arguments, consider trying combinations of "
                            "negative numbers, zero, and positive numbers. All test cases should be written with the function name "
                            "and the assigned values of the arguments. For example, for a function `add(a, b)`, one possible test case "
                            "is `add(5, 3)` or `add(-3, -5)`."
                            ""), None

        for category in CATEGORIES.keys():
            if button_id == f"{category}-button":
                return html.Div([
                    html.H2(f"{category}"),
                    html.Ul([
                        html.Li(dcc.Link(subpage, href=f"/{category}/{subpage}"))
                        for subpage in CATEGORIES[category]
                    ])
                ]), None

    if pathname and pathname != '/':
        path_parts = pathname.strip('/').split('/')
        if len(path_parts) == 2:
            category, subpage = path_parts
            category = category.replace('%20', ' ')

            if category in SUBPAGE_LAYOUTS and subpage in SUBPAGE_LAYOUTS[category]:
                return None, html.Div(SUBPAGE_LAYOUTS[category][subpage])

    return html.P("As the name suggests, unit tests allow you to test your code in isolated small 'units', "
                            "rather than having to test an entire application. In these exercises, the 'unit' to be "
                            "tested is a function that you first need to define. However, it may be helpful to note "
                            "some test cases and their expected outputs before actually writing the function. All "
                            "test cases can be written directly into the grid below each function. Be sure to fill in "
                            "all of the rows with test cases. The number of rows for each table varies for different "
                            "functions. A function with two boolean arguments (True and False) will only have four possible "
                            "test cases (where the arguments are True and True, True and False, False and True, and False and False). "
                            "However, other functions (for example, one with two integer arguments) has an infinite number of "
                            "possible test cases. Therefore, you will need to think of test cases that adequeately test your function. "
                            "This often means considering edge cases. If a function has an argument that is a string, an important "
                            "edge case is an empty string. Similarly, if a function has an argument that is a list, an important "
                            "edge case is an empty list. For functions with integer arguments, consider trying combinations of "
                            "negative numbers, zero, and positive numbers. All test cases should be written with the function name "
                            "and the assigned values of the arguments. For example, for a function 'add(a, b)', one possible test case "
                            "is 'add(5, 3)' or 'add(-3, -5)'."), None

if __name__ == '__main__':
    app.run_server(debug=True)






