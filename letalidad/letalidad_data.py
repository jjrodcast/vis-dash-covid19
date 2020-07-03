import pandas as pd

class LetalidadData:

    def __init__(self):
        self.data = pd.read_csv('letalidad/DataSet_Letalidad.csv')

    def getInfo(self, filters=[]):
        ageGroup = self.getData().groupby(by=['Departamento']).sum()
        ageGroup.reset_index(inplace=True)

        if (filters is not None) and (len(filters) != 0):
            ageGroup = ageGroup[ageGroup['Departamento'].isin(filters)]

        deps = ageGroup['Departamento'].unique()
        values = []

        for dep in deps:
            values.append(ageGroup[((ageGroup['Departamento'] == dep)&(ageGroup['Departamento'] == dep))]['Letalidad(%)'].values[0])
	

        return {'deps': deps, 'values': values}

    def getDepartments(self):
        deps = self.getData().drop_duplicates(['Departamento'])['Departamento'].reset_index(drop=True)
        tdeps = []
        for dep in deps:
        	tdeps.append({'value': dep, 'label': dep})
        return tdeps

    def getData(self):
        return self.data