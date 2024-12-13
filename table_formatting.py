import dash
from dash import dcc, html, dash_table
import pandas as pd
from dash.dependencies import Input, Output

# Sample data
data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [1, 3, 3, 5, 5]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_data_conditional=[
            {
                'if': {
                    'filter_query': '{Column1} != {Column2}'
                },
                'backgroundColor': 'red',
                'color': 'white'
            },
            {
                'if': {
                    'filter_query': '{Column1} = {Column2}'
                },
                'backgroundColor': 'green',
                'color': 'white'
            }
        ],
        style_cell={'textAlign': 'center'},
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)