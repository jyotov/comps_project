from dash import dcc, html, dash_table, callback
from dash.dependencies import Input, Output, State
import pandas as pd

# Initial DataFrame with empty code and output columns
initial_data = {
    'Code': ["", "", "", "", "", ""],
    'Output': ["", "", "", "", "", ""]
}
df = pd.DataFrame(initial_data)

# dash.register_page(__name__)

layout = [
    html.H1(children='draw_star_triangle'),
    html.Div(children=dcc.Markdown('''
            Define a function `draw_star_triangle` that draws a isosceles triangle using the letter 'o' of height equal to the parameter `num`.
            For example, `draw_star_triangle(5)` should output a triangle with one 'o' in the first row, two in the second row,
            five on the fifth row, four on the sixth row, and one on the ninth row.
            '''),
             style={'textAlign': 'left',
                    }),
    dcc.Textarea(
        id='textarea-example',
        value='def draw_star_triangle(num):',
        style={'width': '100%', 'height': 300},  # this is CSS -- you can change the styles
    ),
    # html.Button('Submit', id='submit-val', n_clicks=0),
    # dcc.Input(
    #     id="result",
    #     disabled=True,
    # ),
    html.Div([
        dash_table.DataTable(
            id='result12',
            columns=[
                {"name": "Code", "id": "Code", "editable": True},
                {"name": "Output", "id": "Output"},
                {"name": "Expected", "id": "Expected"}
            ],
            data=df.to_dict('records'),
            style_cell={'fontFamily': 'monospace', 'whiteSpace': 'pre', 'textAlign': 'left'},
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{Output} != {Expected} && {Output} != ""'
                    },
                    'backgroundColor': 'red',
                    'color': 'white',
                },
                {
                    'if': {
                        'filter_query': '{Output} = {Expected} && {Output} != ""'
                    },
                    'backgroundColor': 'green',
                    'color': 'white',
                }

            ],
        ),
        html.Button('Run Tests', id='run-button', style={'margin-top': '10px'}),
    ])
]

# for submit button -> for data table
@callback(
    Output('result12', 'data'),
    Input('run-button', 'n_clicks'),
    State('result12', 'data'),
    State('textarea-example', 'value'),
    config_prevent_initial_callbacks=True
)

def execute_code(n_clicks, rows, value):
    if n_clicks:
        globals = {}
        locals = {}
        exec(value, globals, locals)
        for row in rows:
            code = row.get('Code', '')
            try:
                # Limit scope to only evaluate simple expressions
                local_scope = {}
                exec("result12 = " + code, globals, locals)  # safer for simple expressions
                row['Output'] = locals.get('result12', '')
                locals2 = {"draw_star_triangle":draw_star_triangle}
                exec("result12 = " + code, globals, locals2)  # safer for simple expressions
                row['Expected'] = locals2.get('result12', '')
                # if row['Expected'] == row['Output']:
                #     cases_passed += 1
            except Exception as e:
                row['Output'] = f"Error: {str(e)}"
    return rows

def draw_star_triangle(num):
    for i in range(num): ## 1 to num - 1 star(s)
        print(i * 'o')
    for i in range(num, 0, -1): ## num to 1 star(s)
        print(i * 'o')