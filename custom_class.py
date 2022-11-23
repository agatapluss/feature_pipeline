import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class CustomDrop(BaseEstimator, TransformerMixin):
    
    def __init__(self, drop_col=None):
        self.drop_col = drop_col
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_= X.copy()
    X_= X_.drop(self.drop_col, axis =1)
        return X_