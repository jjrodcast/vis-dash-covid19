import datetime as dt
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html



data_consumos = pd.read_csv('consumos/data/data_consumos_tarjetas.csv', encoding='latin-1')
data_consumos['codmes_transaccion'] = data_consumos['codmes_transaccion'].astype(str)
data_consumos['fecha_transaccion'] = data_consumos['fecha_transaccion'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))


df=data_consumos.copy()

def fx_graficar_evol_compras(valor='transacciones'): # transacciones,monto
    data = df[df['tipo_operacion']=='COMPRAS']
    gb_codmes_trx_mtos = data.groupby('fecha_transaccion',as_index=False).agg({'transacciones':'sum','monto':'sum'})
    
    fig = go.Figure(data = go.Scatter(x = gb_codmes_trx_mtos['fecha_transaccion'], 
                                      y = gb_codmes_trx_mtos[valor]))

    if valor=='transacciones':
        fig.update_layout(title={'text':'Evolución del Número de Transacciones',
                                'font':{'size':28},'x':0.5,'xanchor':'center'},
                            xaxis={'title':'Mes'},
                            yaxis={'title':'Número de Transacciones'})
    elif valor=='monto':
        fig.update_layout(title={'text':'Evolución del Volumen de Compras',
                                'font':{'size':28},'x':0.5,'xanchor':'center'},
                            xaxis={'title':'Mes'},
                            yaxis={'title':'Monto Total de Consumo'})
    
    return(fig)


#Filtros

def radioItems_digital():
    dicc_options = [{'label': 'Compras Presenciales', 'value': 'NODIG'},
                    {'label': 'Compras Digitales', 'value': 'DIG'},
                    {'label': 'Todas', 'value': 'Todas'}]
    return(dcc.RadioItems(
        id='id_radioItems_digital',
        options=dicc_options,
        labelStyle={'display': 'inline-block'},
        value='Todas'
    ) )

def checkList_tipo_tarjeta():
    dicc_options = [{'label': 'Tarjeta de Crédito', 'value': 'TC'},
                    {'label': 'Tarjeta de Débito', 'value': 'TD'}]
    return(dcc.Checklist(
        id='id_checkList_tipo_tarjeta',
        options=dicc_options,
        labelStyle={'display': 'inline-block'}
    ) )

def dropdown_categoria_consumo():
    dicc_options = [{'label': value, 'value': value} for value in df['categoria'].unique()]
    return(dcc.Dropdown(
                id='id_dropdown_categoriaconsumo',
                options=dicc_options,
                multi=True,
                disabled=False,
                clearable=True,
                searchable=True,
                placeholder='Elige una o más opciones..',
                #className='form-dropdown',
                #style={'width':"90%"},
                persistence='string',
                persistence_type='memory'
            ))

def dropdown_subcategoria_consumo():
    dicc_options = [{'label': value, 'value': value} for value in df['subcategoria'].unique()]
    return(dcc.Dropdown(
                id='id_dropdown_subcategoriaconsumo',
                options=dicc_options,
                multi=True,
                disabled=False,
                clearable=True,
                searchable=True,
                placeholder='Elige una o más opciones..',
                #className='form-dropdown',
                #style={'width':"90%"},
                persistence='string',
                persistence_type='memory'
            ))

def radioItems_nacionalidad():
    dicc_options = [{'label': 'Compras Nacionales', 'value': 'NAC'},
                    {'label': 'Compras Internacionales', 'value': 'INT'},
                    {'label': 'Todas', 'value': 'Todas'}]
    return(dcc.RadioItems(
        id='id_radioItems_nacionalidad',
        options=dicc_options,
        labelStyle={'display': 'inline-block'},
        value='Todas'
    ) )


def dropdown_region():
    dicc_options = [{'label': value, 'value': value} for value in df['region'].unique() if value not in ['OTROS','DESCONOCIDO']]
    return(dcc.Dropdown(
                id='id_dropdown_region',
                options=dicc_options,
                multi=True,
                disabled=False,
                clearable=True,
                searchable=True,
                placeholder='Elige una o más opciones..',
                #className='form-dropdown',
                #style={'width':"90%"},
                persistence='string',
                persistence_type='memory'
            ))

def dropdown_grupo_region():
    dicc_options = [{'label': value, 'value': value} for value in df['grupo_region'].unique() if value not in ['OTROS','DESCONOCIDO']]
    return(dcc.Dropdown(
                id='id_dropdown_grupo_region',
                options=dicc_options,
                multi=False,
                disabled=False,
                clearable=True,
                searchable=True,
                placeholder='Elige una de las opciones..',
                #className='form-dropdown',
                #style={'width':"90%"},
                persistence='string',
                persistence_type='memory'
            ))


# Graficos
def fx_graficar_evol_compras_dinamico(valor='transacciones'): # transacciones,monto
    data = df[df['tipo_operacion']=='COMPRAS']
    gb_codmes_trx_mtos = data.groupby('fecha_transaccion',as_index=False).agg({'transacciones':'sum','monto':'sum'})
    
    fig = go.Figure(data = go.Scatter(x = gb_codmes_trx_mtos['fecha_transaccion'], 
                                      y = gb_codmes_trx_mtos[valor]))

    if valor=='transacciones':
        fig.update_layout(title={'text':'Evolución del Número de Transacciones',
                                'font':{'size':28},'x':0.5,'xanchor':'center'},
                            xaxis={'title':'Mes'},
                            yaxis={'title':'Número de Transacciones'})
    elif valor=='monto':
        fig.update_layout(title={'text':'Evolución del Volumen de Compras',
                                'font':{'size':28},'x':0.5,'xanchor':'center'},
                            xaxis={'title':'Mes','zeroline':True},
                            yaxis={'title':'Monto Total de Consumo'})
    
    fig.update_yaxes(range=[0,gb_codmes_trx_mtos[valor].max()*1.05]) 
    
    return(fig)

def fx_actualizar_grafico_compras(sel_digital,sel_cat,sel_subcat,sel_nac,sel_gRegion,sel_region, valor='transacciones'):
    data = df[df['tipo_operacion']=='COMPRAS']
    if sel_digital != 'Todas':
        data = data[data['flg_digital'] == sel_digital]

    if sel_cat is not None and len(sel_cat)!=0:
        data = data[data['categoria'].isin(sel_cat)]
    
    if sel_subcat is not None and len(sel_subcat)!=0:
        data = data[data['subcategoria'].isin(sel_subcat)]

    if sel_nac != 'Todas':
        data = data[data['marca_pais_mov'] == sel_nac]        

    if sel_gRegion is not None:
        data = data[data['grupo_region'] == sel_gRegion]

    if sel_region is not None and len(sel_region)!=0:
        data = data[data['region'].isin(sel_region)]

    gb_codmes_trx_mtos = data.groupby('fecha_transaccion',as_index=False).agg({'transacciones':'sum','monto':'sum'})
    
    
    fig = go.Figure(data = go.Scatter(x = gb_codmes_trx_mtos['fecha_transaccion'], 
                                      y = gb_codmes_trx_mtos[valor]))

    if valor=='transacciones':
        fig.update_layout(title={'text':'Evolución del Número de Transacciones',
                                'font':{'size':28},'x':0.5,'xanchor':'center'},
                            xaxis={'title':'Mes','zeroline':True},
                            yaxis={'title':'Número de Transacciones'})
    elif valor=='monto':
        fig.update_layout(title={'text':'Evolución del Volumen de Compras',
                                'font':{'size':28},'x':0.5,'xanchor':'center'},
                            xaxis={'title':'Mes','zeroline':True},
                            yaxis={'title':'Monto Total de Consumo'})
    
    fig.update_yaxes(range=[0,gb_codmes_trx_mtos[valor].max()*1.05]) 
    
    return(fig)
	

# Funciones Tab Consumos:
def build_tab_consumos():
    return [html.Br(),
            html.Div(
            id="id_desc_info_financiera",
            # className='twelve columns',
            children=[#.H4('Comportamiento de Compras'),
                     html.P("Analizar cómo ha cambiado el comportamiento de compras debido a la Pandemia.",
                            style={'font-style': 'italic'}),
                    ]
            ),
            html.Br(),
            html.P('Seleccionar Tipo de Canal:',style={'color': 'black', 'font-weight': 'bold'}),
            radioItems_digital(),
            html.Br(),

            html.Div(className='row',
                    children=[html.Div(className='four columns',
                                        children=
                                            [ 
                                            html.P("Seleccionar Categoria:",style={'color': 'black', 'font-weight': 'bold'})
                                            ]
                                        ),
                             html.Div(className='four columns',
                                        children=
                                            [
                                            html.P("Seleccionar Subcategoria:",style={'color': 'black', 'font-weight': 'bold'})
                                            ]
                                        )
                            ]
            ),
            html.Div(className='row',
                    children=[html.Div(className='four columns',
                                        children=
                                            [ 
                                            dropdown_categoria_consumo()
                                            ]
                                        ),
                             html.Div(className='four columns',
                                        children=
                                            [
                                            dropdown_subcategoria_consumo()
                                            ]
                                        )
                            ]
            ),
            html.Br(),
            
            html.P('Seleccionar Tipo de Compras:',style={'color': 'black', 'font-weight': 'bold'}),
            radioItems_nacionalidad(),
            
            html.Br(),
            html.Div(className='row',
                    children=[html.Div(className='four columns',
                                        children=
                                            [ 
                                            html.P("Seleccionar Macro Región:",style={'color': 'black', 'font-weight': 'bold'})
                                            ]
                                        ),
                             html.Div(className='four columns',
                                        children=
                                            [
                                            html.P("Seleccionar Departamento:",style={'color': 'black', 'font-weight': 'bold'})
                                            ]
                                        )
                            ]
            ),

            html.Div(className='row',
                    children=[html.Div(className='four columns',
                                        children=
                                            [ 
                                            dropdown_grupo_region()
                                            ]
                                        ),
                              html.Div(className='four columns',
                                        children=
                                            [ 
                                            dropdown_region()
                                            ]
                                        )
                            ]
            ),

            html.Div(
                id='id_div_evol',
                children=[
                dcc.Graph(
                    id="id_graf_evol_transacciones_dinamico",
                    figure=fx_graficar_evol_compras_dinamico(valor='transacciones')
                ),
                
                dcc.Graph(
                    id="id_graf_evol_monto_dinamico",
                    figure=fx_graficar_evol_compras_dinamico(valor='monto')
                )])
            ]