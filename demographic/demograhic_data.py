import pandas as pd

class DemographicData:

    def __init__(self):
        self.data = pd.read_csv('demographic/covid_positive_vs_death.csv')

    def getInfoByAgeGroup(self, filter_type=None, filters=[]):
        ageGroup = self.getData().groupby(by=['COD', 'DEPARTAMENTO', 'GRUPO_EDAD']).sum()
        ageGroup.reset_index(inplace=True)

        col = 'TOTAL_FALLECIDOS' if filter_type == 'CF' else 'TOTAL_POSITIVOS'

        if len(filters) != 0:
            ageGroup = ageGroup[ageGroup['COD'].isin(filters)]


        cods = ageGroup['COD'].unique() 
        deps = ageGroup['DEPARTAMENTO'].unique()
        ages = ageGroup['GRUPO_EDAD'].unique()
        values = []

        for age in ages:
            vals = []
            for cod in cods:
                vals.append(ageGroup[((ageGroup['COD'] == cod)&(ageGroup['GRUPO_EDAD'] == age))][col].values[0])
            values.append(vals)
        return {'name': ages, 'cods': cods, 'x': deps, 'y': values}

    def getInfoBySexGroup(self, filter_type=None, filters=[]):
        sexGroup = self.getData().groupby(by=['COD', 'DEPARTAMENTO', 'SEXO']).sum()
        sexGroup.reset_index(inplace=True)

        col = 'TOTAL_FALLECIDOS' if filter_type == 'CF' else 'TOTAL_POSITIVOS'

        if len(filters) != 0:
            sexGroup = sexGroup[sexGroup['COD'].isin(filters)]

        cods = sexGroup['COD'].unique() 
        deps = sexGroup['DEPARTAMENTO'].unique()
        sexs = sexGroup['SEXO'].unique()
        values = []

        for sex in sexs:
            vals = []
            for cod in cods:
                vals.append(sexGroup[((sexGroup['COD'] == cod)&(sexGroup['SEXO'] == sex))][col].values[0])
            values.append(vals)

        return {'name': sexs, 'cods': cods, 'x': deps, 'y': values}

    def getLocations(self):
        return [{'label': 'Casos Positivos', 'value': 'CP'}, {'label': 'Casos Fallecidos', 'value': 'CF'}]

    def getDepartments(self):
        deps = self.getData().drop_duplicates(['COD', 'DEPARTAMENTO'])[['COD', 'DEPARTAMENTO']].reset_index(drop=True)
        deps = deps.values
        tdeps = []
        for dep in deps:
            tdeps.append({'label': dep[1], 'value': dep[0]})
        return tdeps

    def getData(self):
        return self.data