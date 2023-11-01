from dash import html

def sidebar_item(item_symbol:str='person', item_text:str='icon text', item_href:str='#'):
    return html.A(
        href=item_href,
        children=[
            html.Span(
                className="material-icons-sharp",
                children=item_symbol
            ),
            html.H3(
                children=item_text
            )
        ]
    )