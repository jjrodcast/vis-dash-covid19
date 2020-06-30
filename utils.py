import dash_html_components as html
import dash_core_components as dcc

def create_title(app, title):
    app.title = title

def create_header(app):
    logo = html.Img(id='logo', src=app.get_asset_url('logo.png'))
    h4 = html.H4(children="Visualización de Datos")
    p = html.P(id='description',
              children='El proyecto muestra información relacionada al COVID-19 \
              que en estos últimos meses ha afectado a toda la población. Los datos mostrados son los que nos brinda el MINSA.')
    return [logo, h4, p]

def create_tabs():
    tab_items = [
        dcc.Tab(label='Tab 1', value='tab1'),
        dcc.Tab(label='Tab 2', value='tab2'),
        dcc.Tab(label='Tab 3', value='tab3'),
        dcc.Tab(label='Positivos / Fallecidos', value='tab4'),
        dcc.Tab(label='Tab 5', value='tab5')
    ]

    tabs = dcc.Tabs(id='tabs', value='tab4', children=tab_items)
    content = html.Div(id='tabs-content')

    return [tabs, content]