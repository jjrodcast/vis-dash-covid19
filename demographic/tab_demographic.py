import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def __create_filters(types, depts):
    labelType = html.P(children='Seleccionar tipo:')
    selectorTypes = dcc.Dropdown(id='dd-type', clearable=False, value='CP', options=types)

    labelDep = html.P(children='Seleccionar Departamentos:')
    selectorDep = dcc.Dropdown(id='dd-dep', options=depts, value='', multi=True, placeholder='Departamentos')

    return ([labelType, selectorTypes],[labelDep, selectorDep])

def create_demographic(types, depts, data = None):
    title = html.H4(children='Casos Positivos y Fallecidos', className='center')
    
    _types, _deps = __create_filters(types, depts)

    left =  html.Div(className='six columns', children=_types)
    right = html.Div(className='six columns', children=_deps)

    containerFilters = html.Div(className='row', children=[left, right])
    
    graphic_by_age = dcc.Graph(id='graph_cases_by_age', figure=create_age_group_layout(data))
    graphic_by_sex = dcc.Graph(id='graph_cases_by_sex', figure=create_sex_group_layout(data))
    
    #graphic_left = html.Div(className='six columns', children=[graphic_by_age])
    #graphic_right = html.Div(className='six columns', children=[graphic_by_sex])

    containerLayout = html.Div(className='row', children=[graphic_by_age, graphic_by_sex])
    
    container = html.Div(children=[title, containerFilters, containerLayout])

    return container

def create_age_group_layout(data):
    names = data['name']
    xs = data['x']
    ys = data['y']
    bars = []
    for name, y in zip(names, ys):
        bars.append(go.Bar(name=name, x=xs, y=y))
    
    figure = go.Figure(data=bars)
    figure.update_layout(title='Información por Grupo de Edad', barmode='stack', xaxis_tickangle=-45)
    return figure

def create_sex_group_layout(data):
    names = data['name']
    xs = data['x']
    ys = data['y']
    bars = []
    for name, y in zip(names, ys):
        bars.append(go.Bar(name=name, x=xs, y=y))
    
    figure = go.Figure(data=bars)
    figure.update_layout(title='Información por Sexo', barmode='stack', xaxis_tickangle=-45)
    return figure