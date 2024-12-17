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
    html.H1(children='days_in_month'),
    html.Div(children=dcc.Markdown('''
            Return the number of days in a given month. The argument `month` is a string of a month (such as `March`).
            For February, `leap_year` will tell you whether it is a leap year, in which case February has 29 days. Otherwise,
            it has 28 days. Return `Invalid month` if the argument `month` is not properly formatted.
            '''),
             style={'textAlign': 'left',
                    }),
    dcc.Textarea(
        id='textarea-example',
        value='def days_in_month(month, leap_year):',
        style={'width': '100%', 'height': 300},  # this is CSS -- you can change the styles
    ),
    # html.Button('Submit', id='submit-val', n_clicks=0),
    # dcc.Input(
    #     id="result",
    #     disabled=True,
    # ),
    html.Div([
        dash_table.DataTable(
            id='result4',
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
    Output('result4', 'data'),
    Input('run-button', 'n_clicks'),
    State('result4', 'data'),
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
                exec("result4 = " + code, globals, locals)  # safer for simple expressions
                row['Output'] = locals.get('result4', '')
                locals2 = {"days_in_month":days_in_month}
                exec("result4 = " + code, globals, locals2)  # safer for simple expressions
                row['Expected'] = locals2.get('result4', '')
                # if row['Expected'] == row['Output']:
                #     cases_passed += 1
            except Exception as e:
                row['Output'] = f"Error: {str(e)}"
    return rows

def days_in_month(month, leap_year):
    if month == "January":
        return 31
    elif month == "February":
        return 29 if leap_year else 28
    elif month == "March":
        return 31
    elif month == "April":
        return 30
    elif month == "May":
        return 31
    elif month == "June":
        return 30
    elif month == "July":
        return 31
    elif month == "August":
        return 31
    elif month == "September":
        return 30
    elif month == "October":
        return 31
    elif month == "November":
        return 30
    elif month == "December":
        return 31
    else:
        return "Invalid month"
