from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            children = "Hello, James"
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

# gunicorn --bind=0.0.0.0 --timeout 600 app:server