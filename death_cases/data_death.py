import pandas as pd

class DeathData:
    
    def datos(self):
        df_positivos = pd.read_csv('death_cases/positivos_covid.csv')
        df_positivos['date'] = pd.to_datetime(df_positivos['FECHA_RESULTADO'], dayfirst=True, format = '%d/%m/%Y')
        df_positivos.columns = [i.lower() for i in df_positivos.columns]
        
        df_fallecidos = pd.read_csv('death_cases/fallecidos_covid.csv')
        df_fallecidos['date'] = pd.to_datetime(df_fallecidos['FECHA_FALLECIMIENTO'], dayfirst=True, format = '%d/%m/%Y')
        df_fallecidos.columns = [i.lower() for i in df_fallecidos.columns]
        
        """ TRANSFORM DATA """
        
        uid = ['uuid']
        variables = ['departamento','date']

        m = df_positivos[variables+uid].groupby(variables).agg(['count']).reset_index()
        m.columns = variables + ['Positivos']

        n = df_fallecidos[variables+uid].groupby(variables).agg(['count']).reset_index()
        n.columns = variables + ['Fallecidos']

        df = m.merge(n, on = variables,how='outer')

        df['Positivos'].fillna(0,inplace=True)
        df['Fallecidos'].fillna(0,inplace=True)
        
        df = df.melt(id_vars=["departamento", "date"], var_name="caso", value_name="frecuencia")
        df_dist = df.pivot_table(['frecuencia'],['date','caso'],'departamento',aggfunc='sum', fill_value=0).reset_index()
        
        """ MODIFY NAMES COLUMNS """
        
        nombres = []
        for x in df_dist.columns:
            if x[1]== '':
                nombres.append(x[0])
            else:
                nombres.append(x[1])

        df_dist.columns = nombres
        
        """ SEPARATE POSITIVES FROM DEATHS """
        
        fallecidos = df_dist.loc[df_dist.caso=='Fallecidos'].drop('caso',axis=1)
        positivos = df_dist.loc[df_dist.caso=='Positivos'].drop('caso',axis=1)

        fallecidos.set_index('date', inplace=True)
        positivos.set_index('date', inplace=True)
        
        positivos['TOTAL'] = positivos.sum(axis=1)
        fallecidos['TOTAL'] = fallecidos.sum(axis=1)
        
        return positivos,fallecidos