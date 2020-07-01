import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

def create_days_r(deps):
    br = html.Br()

    title = html.H4('Visualizando R0', className='center')
    deps = dcc.Dropdown(id='departamentos', options=deps, value='por_dia')

    dep_name = html.P(id='dprt')
    slider = dcc.Slider(id='tiempo', 
                        min=1, 
                        max=15, 
                        step=5,
                        marks={1: '1 Dia', 5: '5 Dias', 10: '10 Dias', 15: '15 Dias',},
                        value=1)

    row = html.Div(className='row', children=[dep_name, slider])


    graphic = dcc.Graph(id='por_dia')

    container = html.Div(
        id='contenedor-days',
        children=[title, deps, br, row, graphic]
    )

    return container

def create_days_figure(dprto, tiempo, data):
    if dprto == 'por_dia':
        container = 'Todo Perú'
    else:
        container = 'Departamento ' + dprto

    if tiempo == 1:
        if dprto == 'por_dia':
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por dia nivel nacional')
        else:
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por dia '+ dprto)
    if tiempo == 5:
        if dprto == 'por_dia':
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por dia nivel nacional')
        else:
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por dia '+ dprto)
    if tiempo == 10:
        if dprto == 'por_dia':
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por 10 dias a nivel nacional')
        else:
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por 10 dias '+ dprto)
    if tiempo == 15:
        if dprto == 'por_dia':
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por 15 dias a nivel nacional')
        else:
            fig = px.line(data, x='Fecha', y='R0_'+ dprto, title='R0 por 15 dias '+ dprto)

    return container, fig