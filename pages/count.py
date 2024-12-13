import dash
from dash import dcc, html, dash_table, callback
from dash.dependencies import Input, Output, State
import pandas as pd

# Initial DataFrame with empty code and output columns
initial_data = {
    'Test Cases': ["", "", "", "", "", ""],
    'Output': ["", "", "", "", "", ""]
}
df = pd.DataFrame(initial_data)

#dash.register_page(__name__)

count = 0

layout = [
    html.H1(children='count'),
    html.Div(children=dcc.Markdown('''
            Define a function called `count` that has two arguments: `lst` and `item`. Return the number of times the 
            item occurs in the list.
            
            `count([1, 2, 1, 1], 1) → 3`
            
            `count([], 1) → 0`
            
            `count([2, 4, 6, 8], 3) → 0`
            '''),
             style={'textAlign': 'left',
                    }),
    dcc.Textarea(
        id='textarea-example',
        value='def count(lst, item):',
        style={'width': '100%', 'height': 300},  # this is CSS -- you can change the styles
    ),
    # html.Button('Submit', id='submit-val', n_clicks=0),
    # dcc.Input(
    #     id="result",
    #     disabled=True,
    # ),
    html.Div([
        dash_table.DataTable(
            id='result2',
            columns=[
                {"name": "Test Cases", "id": "Code", "editable": True},
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
                },
                # {
                #     "if": {"state": "active"},
                #     "backgroundColor": "inherit",
                #     "border": "inherit",
                # },
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit",  # Inherit styling from conditional rules
                    "border": "none",  # Optional: Remove the border
                },
                # {
                #     'if': {
                #         'filter_query': '{Output} != ""'
                #     },
                #     'backgroundColor': 'white',
                #     'color': 'white',
                # }
            ],
        ),
        html.Button('Run Tests', id='run-button', style={'margin-top': '10px'}),
    ])
]

# for submit button -> for data table
@callback(
    Output('result2', 'data'),
    Input('run-button', 'n_clicks'),
    State('result2', 'data'),
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
                exec("result2 = " + code, globals, locals)  # safer for simple expressions
                row['Output'] = locals.get('result2', '')
                locals2 = {"count":count}
                exec("result2 = " + code, globals, locals2)  # safer for simple expressions
                row['Expected'] = locals2.get('result2', '')
            except Exception as e:
                row['Output'] = f"Error: {str(e)}"
    return rows

def count(lst, item):
    count = 0
    for x in lst:
        if x == item:
            count += 1
    return count
