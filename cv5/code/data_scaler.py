from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

class DataScaler:

    def __init__(self):
            self.scaler = RobustScaler()

    def fit_transform(self, data):
        return self.scaler.fit_transform(data)

    def transform(self, data):
        return self.scaler.transform(data)
