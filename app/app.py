import os
from dash import Dash, html

from components import *

app = Dash(
    __name__,
    external_stylesheets=["https://fonts.googleapis.com/icon?family=Material+Icons+Sharp"]
)
server = app.server

app.layout = html.Main(
    children=[
        html.Title(
            children="My Profile"
        ),
        html.Div(
            className='container',
            children=[
                html.Aside(
                    children=[
                        html.Div(
                            className='toggle',
                            children=[
                                my_logo, 
                                html.Div(
                                    className='close',
                                    children=[
                                        html.Span(
                                            className='material-icons-sharp',
                                            children='close'
                                        )
                                    ]
                                )
                            ]
                        ), 
                        html.Div(
                            className='sidebar',
                            children=[
                                sidebar_item(item_symbol='account_circle', item_text='About me'),
                                sidebar_item(item_symbol='dashboard', item_text='Dashboard'),
                                sidebar_item(item_symbol='logout', item_text='Logout')
                            ]
                        )
                    ]
                ),
                html.Div(
                    className='main-content', 
                    children=[
                        html.H1("Analytics"),
                        html.Div(
                            className="analysis",
                            children=[
                                lead_card(
                                    card_title="First key stat"
                                ),
                                lead_card(
                                    card_title="Another Key stat"
                                ),
                                lead_card(
                                    card_title="Final key stat"
                                ),
                            ]
                        ),
                        html.Div(
                            className='new-users',
                            children=[
                                html.H2('New Users')
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
