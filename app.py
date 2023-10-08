from dash import Dash, html
import flask

server = flask.Flask(__name__)
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
    app.run(debug=True, port=8000)

# gunicorn --bind=0.0.0.0 --timeout 600 app:server
