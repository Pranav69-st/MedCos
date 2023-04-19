import pandas as pd
import pickle

class DoctorConsultationFeeModel:
    def __init__(self):
        with open('docfee.pkl', 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, X):
        return self.model.predict(X)
