import json
import dash_html_components as html
import dash_core_components as dcc

def create_title(app, title):
    app.title = title

def create_header(app):
    logo = html.Img(id='logo', src=app.get_asset_url('logo.png'))
    h4 = html.H4(children="Visualización de Datos")
    p = html.P(id='description',
              children='El proyecto muestra información relacionada al COVID-19 \
              que en estos últimos meses ha afectado a toda la población. Los datos mostrados son los que nos brinda el MINSA. Datos actualizados hasta el 10/06/2020')
    return [logo, h4, p]

def create_tabs():
    tab_items = [
        dcc.Tab(label='Pruebas Rápidas y Moleculares', value='tab1'),
        dcc.Tab(label='Contagios y Fallecidos', value='tab2'),
        dcc.Tab(label='Tasa de Letalidad', value='tab3'),
        dcc.Tab(label='Información por Edad y Sexo', value='tab4'),
        dcc.Tab(label='Tasa de Contagio', value='tab5'),
        dcc.Tab(label='Comportamiento de Compras', value='tab6')
    ]

    tabs = dcc.Tabs(id='tabs', value='tab6', children=tab_items)
    content = html.Div(id='tabs-content')

    return [tabs, content]

def get_geojson():
    peru_geoson = None
    with open('map/peru_departamental_simple.geojson') as f:
        peru_geoson = json.load(f)
    return peru_geoson