import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

def __create_filters(types, depts):
    labelType = html.P(children='Seleccionar Pruebas:')
    selectorTypes = dcc.Dropdown(id='dd-prove-type', clearable=False, value='PR', options=types)

    labelDep = html.P(children='Seleccionar Departamentos:')
    selectorDep = dcc.Dropdown(id='dd-prove-dep', options=depts, value='', multi=True, placeholder='Departamentos')

    return ([labelType, selectorTypes],[labelDep, selectorDep])

def create_proves(types, depts, _type, _geojson, data):
    title = html.H4(children='Pruebas PCR / PR', className='center')
    title_table = html.H4(children='Información General', className='center')
    _types, _deps = __create_filters(types, depts)

    left =  html.Div(className='six columns', children=_types)
    right = html.Div(className='six columns', children=_deps)
    containerFilters = html.Div(className='row', children=[left, right])

    graphic_map = dcc.Graph(id='graph_map_proves', figure=create_map_proves_figure(_type, _geojson, data))

    containerGraphics = html.Div(className='row', children=[graphic_map])

    info = html.Div(id='info_prove_dept')

    container =  html.Div(children=[title, containerFilters, containerGraphics, info])

    return container

def create_map_proves_figure(_type, _geojson, data):
    title = 'Pruebas Rápidas por Departamento' if _type == 'PR' else 'Pruebas Moleculares por Departamento'

    figure = px.choropleth(data, 
        geojson=_geojson,
        color=_type,
        color_continuous_scale='Reds',
        locations='NOMBDEP',
        featureidkey='properties.NOMBDEP')

    figure.update_geos(fitbounds='locations', visible=False)
    figure.update_layout(clickmode='event+select', title_text=title)

    return figure

def create_info(data):
    _dep = data['NOMBDEP'].values[0]
    _pr = data['PR'].values[0]
    _pcr = data['PCR'].values[0]
    dept = html.Div(className='row', children=[html.Span('DEPARTAMENTO: ', style={'fontWeight': 'bold'}), html.Span(_dep)])
    pr = html.Div(className='row', children=[html.Span('PRUEBAS RÁPIDAS: ', style={'fontWeight': 'bold'}), html.Span(f'{int(_pr):,}')])
    pcr = html.Div(className='row', children=[html.Span('PRUEBAS MOLECULARES: ', style={'fontWeight': 'bold'}), html.Span(f'{int(_pcr):,}')])

    return html.Div(children=[dept, pr, pcr])