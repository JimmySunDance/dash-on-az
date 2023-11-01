from dash import html

def lead_card(card_title:str='title', card_value:str='999,999', graph_loc:str='/assets/graph.png'):
    return html.Div(
        className='lead-card',
        children=[
            html.Div(
                className='status',
                children=[
                    html.Div(
                        className='info',
                        children=[
                            html.H3(card_title),
                            html.H1(card_value)
                        ]
                    ), 
                    html.Div(
                        className='card-graph',
                        children=[html.Img(src=graph_loc)]
                    )
                ]
            )
        ]
    )