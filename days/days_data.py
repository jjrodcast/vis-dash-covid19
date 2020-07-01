import pandas as pd

class DaysData:

    def __init__(self):
        self.by_dept = pd.read_csv('days/Por_dept.csv')
        self.five_days = pd.read_csv('days/Por_5Dias.csv')
        self.ten_days = pd.read_csv('days/Por_10Dias.csv')
        self.fiftheen_days = pd.read_csv('days/Por_15Dias.csv')
        self.deps = [{'label': 'Todos los departamentos', 'value':'por_dia'},
                    {'label': 'Amazonas', 'value':'AMAZONAS'},
                    {'label': 'Ancash', 'value':'ANCASH'},
                    {'label': 'Apurimac', 'value':'APURIMAC'},
                    {'label': 'Arequipa', 'value':'AREQUIPA'},
                    {'label': 'Ayacucho', 'value':'AYACUCHO'},
                    {'label': 'Cajamarca', 'value':'CAJAMARCA'},
                    {'label': 'Callao', 'value':'CALLAO'},
                    {'label': 'Cusco', 'value':'CUSCO'},
                    {'label': 'Huancavelica', 'value':'HUANCAVELICA'},
                    {'label': 'Huanuco', 'value':'HUANUCO'},
                    {'label': 'Ica', 'value':'ICA'},
                    {'label': 'Junin', 'value':'JUNIN'},
                    {'label': 'La Libertad', 'value':'LA LIBERTAD'},
                    {'label': 'Lambayeque', 'value':'LAMBAYEQUE'},
                    {'label': 'Lima', 'value':'LIMA'},
                    {'label': 'Loreto', 'value':'LORETO'},
                    {'label': 'Madre De Dios', 'value':'MADRE DE DIOS'},
                    {'label': 'Moquegua', 'value':'MOQUEGUA'},
                    {'label': 'Pasco', 'value':'PASCO'},
                    {'label': 'Piura', 'value':'PIURA'},
                    {'label': 'Puno', 'value':'PUNO'},
                    {'label': 'San Martin', 'value':'SAN MARTIN'},
                    {'label': 'Tacna', 'value':'TACNA'},
                    {'label': 'Tumbes', 'value':'TUMBES'},
                    {'label': 'Ucayali', 'value':'UCAYALI'}]

    
    def getInfoByTime(self, time):
        if time == 1:
            return self.by_dept
        elif time == 5:
            return self.five_days
        elif time == 10:
            return self.ten_days
        elif time == 15:
            return self.fiftheen_days
           
    def getDepartamentos(self):
        return self.deps