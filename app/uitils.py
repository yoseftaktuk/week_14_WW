import pandas as pd

class Data_processing:
    def __init__(self, data):
        self.df = pd.read_csv(data)
        self.add_risk_level()
        self.fix_ampty()
    def add_risk_level(self):
        self.df['risk_level'] = pd.cut(x=self.df['range_km'], bins=[0 , 20 , 100 ,300, 100000000], labels=['low', 'medium', 'high', 'extreme'])

    def fix_ampty(self):
        self.df['manufacturer'] = self.df['manufacturer'].fillna('Unknown', inplace=True)  
        
