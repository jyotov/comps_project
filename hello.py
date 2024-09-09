from dash import Dash, html, dcc, callback, Output, Input, State

app = Dash()

# other components from https://dash.plotly.com/dash-core-components/input
# doc: https://docs.google.com/document/d/1xv4Elh_HFrELS-goC2hW1_Nv90O_R3M-T3Inai_4N0A/edit

app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Textarea(
        id='textarea-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '100%', 'height': 300}, # this is CSS -- you can change the styles
    ),
    html.Button('Submit', id='submit-val', n_clicks=0),
    dcc.Input(
        id="result",
        disabled=True,
    )
]

@callback(
    Output('result', 'value'),
    Input('submit-val', 'n_clicks'),
    State('textarea-example', 'value'),
    config_prevent_initial_callbacks=True
)
def update_graph(_: int, code: str) -> str:
    globals = {}
    locals = {}
    exec(code, globals, locals)
    return str(locals.get("result"))
    # return str((globals,locals))

if __name__ == '__main__':
    app.run(debug=True)
