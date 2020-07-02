import pandas as pd

class ProvesData:

    def __init__(self):
        self.data = pd.read_csv('proves/resumen.csv')
    

    def getProvesType(self):
        return [{'label': 'Pruebas Rápidas', 'value': 'PR'}, {'label': 'Pruebas Moleculares', 'value': 'PCR'}]

    def getDepartments(self):
        deps = self.getData().drop_duplicates(['COD', 'NOMBDEP'])[['COD', 'NOMBDEP']].reset_index(drop=True)
        deps = deps.values
        tdeps = []
        for dep in deps:
            tdeps.append({'label': dep[1], 'value': dep[0]})
        return tdeps

    def getData(self, _type = 'PR', deps=[]):
        data =  self.data.copy()
        
        if len(deps) != 0:
            rows = data[~data['COD'].isin(deps)]
            rows = rows.index.values.tolist()
            data.loc[rows, _type] = 0
            
        return data