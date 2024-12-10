
import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Product Management Dashboard"),
    dcc.Graph(
        figure={
            'data': [
                {'x': ['Feature A', 'Feature B', 'Feature C'], 'y': [10, 20, 15], 'type': 'bar', 'name': 'Adoption Rate'}
            ],
            'layout': {
                'title': 'Feature Adoption Metrics'
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
            