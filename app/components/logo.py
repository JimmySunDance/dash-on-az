from dash import html

my_logo = html.Div(
    className='logo',
    children=[
        html.Img(
            src='assets/atom.png'
        ),
        html.H1(
            className='danger',
            children="JPoulten"
        )
    ]
)