import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from utils import get_geojson
import json
import pandas as pd

def __create_filters(depts):
    labelDep = html.P(children='Seleccionar Departamentos:')
    selectorDep = dcc.Dropdown(id='dd-dep-plot', options=depts, multi=True, placeholder='Departamentos')
    return ([labelDep, selectorDep])

def create_barplot(depts, data = None):
    title = html.H4(children='Porcentaje de Letalidad PERU - COVID19', className='center')
    
    _deps = __create_filters(depts)
    filters =  html.Div(className='six columns', children=_deps)
    containerFilters = html.Div(className='row', children=[filters])
    
    graphic_barplot = dcc.Graph(id='graph_bar', figure=create_barplot_layout(data))
    graphic_map = dcc.Graph(id='graph_map', figure=create_map())    

    container_map = html.Div(className='six columns', children=[graphic_map])
    container_barplot = html.Div(className='six columns', children=[graphic_barplot])
    containerLayout = html.Div(className='row', children=[container_map,container_barplot])

    container = html.Div(children=[title, containerFilters, containerLayout])
    return container

def create_barplot_layout(data):
    xs = data["deps"]
    ys = data["values"]
    max_value = max(ys)
    colors = []
    for i in range(len(ys)):
        colors.append('lightslategrey')
        if (ys[i] == max_value):
            max_index = i
    colors[max_index] = "crimson"
    figure = go.Figure(go.Bar(x=xs, y=ys,marker_color=colors))
    return figure

def create_map():
    df = pd.read_csv('letalidad/DataSet_Letalidad.csv')
    fig = px.choropleth(df, geojson=get_geojson(), color="Letalidad(%)",color_continuous_scale="Reds",locations="Departamento", featureidkey="properties.NOMBDEP")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig