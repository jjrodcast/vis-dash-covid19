# Dash dependencies
import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Pandas dependencies
import pandas as pd

# Utils
from utils import *

# Tabs
from days.tab_days import *
from days.days_data import *

from demographic.tab_demographic import *
from demographic.demograhic_data import *

#region Data
demographic = DemographicData()
data = demographic.getInfoByAgeGroup()

daysData = DaysData()
daysDep = daysData.getDepartamentos()
#endregion

#region Configuración Dash
app = dash.Dash(
    __name__,
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0' }],
)
app.config['suppress_callback_exceptions'] = True
#endregion

#region Creación de Layout
create_title(app, 'Proyecto de Visualización de Datos')

app.layout = html.Div(
    id='root',
    children=[
        html.Div(id='header', children=create_header(app)),
        html.Div(id='container', children=[html.Div(className='row', children=create_tabs())])
    ]
)
#endregion

#region Callback Tabs
@app.callback(Output('tabs-content','children'),
              [Input('tabs','value')])
def render_tabs(tab):
    if tab == 'tab1':
        return html.Div([html.H4('Visualización de Datos')])
    elif tab == 'tab2':
        return create_days_r(daysDep)
    elif tab == 'tab3':
        return html.Div([html.H4('Tab 3 Content')])
    elif tab == 'tab4':
        return create_demographic(demographic.getLocations(), demographic.getDepartments(), data)
    elif tab == 'tab5':
        return html.Div([html.H4('Tab 5 Content')])                
#endregion 

#region Callback Demographic
@app.callback(Output('graph_cases_by_age', 'figure'),
              [Input('dd-type', 'value'), Input('dd-dep', 'value')])
def render_age_group(_type, deps):
    data = demographic.getInfoByAgeGroup(_type, deps)
    return create_age_group_layout(data)

@app.callback(Output('graph_cases_by_sex', 'figure'),
              [Input('dd-type', 'value'), Input('dd-dep', 'value')])
def render_sex_group(_type, deps):
    data = demographic.getInfoBySexGroup(_type, deps)
    return create_sex_group_layout(data)
#endregion

#region Callback Days
@app.callback(
    [Output(component_id='dprt', component_property='children'),
    Output(component_id='por_dia', component_property='figure')],
    [Input(component_id='departamentos', component_property='value'),
    Input(component_id='tiempo', component_property='value')])
def render_days_data(dprto, tiempo):
    print(dprto, tiempo)
    ddata = daysData.getInfoByTime(tiempo)
    return create_days_figure(dprto, tiempo, ddata)
#endregion

#region Ejecutar página
if __name__ == '__main__':
    app.run_server(debug=True)
#endregion