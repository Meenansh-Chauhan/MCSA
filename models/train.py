# models/train.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from preprocessing.sync import synchronize
from preprocessing.filtering import filter_signals
from preprocessing.segmentation import segment_signal
from feature_engineering.fusion import build_feature_dataframe
from preprocessing.normalization import FeatureNormalizer

# ==============================
# SIMULATE LABELS (TEMPORARY)
# ==============================

def generate_labels(n):
    """
    0 = Normal
    1 = Fault
    """
    return np.random.randint(0, 2, size=n)


# ==============================
# TRAIN MODEL
# ==============================

def train_model():
    
    print("Starting training pipeline...\n")
    
    # Step 1: Data pipeline
    df = synchronize()
    df = filter_signals(df)
    segments = segment_signal(df)
    
    # Step 2: Feature extraction
    feature_df = build_feature_dataframe(segments)
    
    # Step 3: Labels (temporary)
    y = generate_labels(len(feature_df))
    
    # Step 4: Normalize features
    normalizer = FeatureNormalizer()
    X = normalizer.fit_transform(feature_df)
    
    # Step 5: Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Step 6: Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Step 7: Accuracy
    accuracy = model.score(X_test, y_test)
    
    print(f"Model trained successfully!")
    print(f"Accuracy: {accuracy:.2f}")
    
    return model, normalizer


# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    train_model()