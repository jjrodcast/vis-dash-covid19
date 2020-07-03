from _plotly_future_ import v4_subplots
import warnings 
import numpy as np
warnings.filterwarnings("ignore")

from plotly import graph_objs as go
from plotly.subplots import make_subplots

class Graphic:
    
    def Grap_Time_Serie(self,posi,death):
        
        # Indica que graficas serán visibles para según el menú desplegable
        vis = []
        for i in np.arange(0,26):
            a=[False]*52
            a[i] = True; a[26+i] = True
            vis.append(a)

        # Create traces
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Plots de casos positivos
        fig.add_trace(go.Scatter(x=posi.index, y=posi.iloc[:,0],mode='lines',name='Positivos',visible=True),secondary_y=False)

        for i in range(1,26):
            fig.add_trace(go.Scatter(x=posi.index, y=posi.iloc[:,i],mode='lines',name='Positivos',visible=False),secondary_y=False)

        # Plots de casos fallecidos
        fig.add_trace(go.Scatter(x=death.index, y=death.iloc[:,0],mode='lines',name='Fallecidos',visible=True),secondary_y=True)

        for j in range(1,26):
            fig.add_trace(go.Scatter(x=death.index, y=death.iloc[:,j],mode='lines',name='Fallecidos',visible=False),secondary_y=True)


        updatemenu=[]
        buttons=[]

        for i in range(0,26):
            lista = list(death.columns)[i],i
            buttons.append(dict(
                                label=lista[0],
                                visible=True,
                                args = [{"visible": vis[i]}])
                                )


        # some adjustments to the updatemenus
        updatemenu=[]
        your_menu=dict()
        updatemenu.append(your_menu)

        updatemenu[0]['buttons']=buttons
        updatemenu[0]['direction']='down'
        updatemenu[0]['showactive']=True

        fig.update_layout(showlegend=True, updatemenus=updatemenu,
                         title_text="Distribución de casos positivos y fallecidos por departamento")


        return fig

    def Grap_Bars(self, tend_alta, tend_baja):

        fig = make_subplots(rows=1, cols=2)

        y = list(tend_alta['b1'])
        x = list(tend_alta['departamento'])

        fig.add_trace(go.Bar(x=x, y=y, name='Tendencia Alta'), row=1, col=1)

        y1 = list(tend_baja['b1'])
        x1 = list(tend_baja['departamento'])

        fig.add_trace(go.Bar(x=x1, y=y1, name='Tendencia Baja'), row=1, col=2)

        fig.update_layout(title_text='Principales Departamentos con Tendencia en el Tiempo a ser Positivos')

        return fig