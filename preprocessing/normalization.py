# preprocessing/normalization.py

import numpy as np
from sklearn.preprocessing import StandardScaler

# ==============================
# NORMALIZATION CLASS
# ==============================

class FeatureNormalizer:
    
    def __init__(self):
        self.scaler = StandardScaler()
    
    def fit(self, X):
        """
        Fit scaler on training data
        """
        self.scaler.fit(X)
    
    def transform(self, X):
        """
        Transform features
        """
        return self.scaler.transform(X)
    
    def fit_transform(self, X):
        """
        Fit + transform
        """
        return self.scaler.fit_transform(X)