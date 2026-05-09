# models/predict.py

import numpy as np

from preprocessing.sync import synchronize
from preprocessing.filtering import filter_signals
from preprocessing.segmentation import segment_signal
from feature_engineering.fusion import build_feature_dataframe
from preprocessing.normalization import FeatureNormalizer
from models.train import train_model

# ==============================
# PREDICTION FUNCTION
# ==============================

def predict_fault():
    
    print("Starting prediction pipeline...\n")
    
    # Step 1: Train model (temporary)
    model, normalizer = train_model()
    
    # Step 2: Get new data
    df = synchronize()
    df = filter_signals(df)
    segments = segment_signal(df)
    
    # Step 3: Feature extraction
    feature_df = build_feature_dataframe(segments)
    
    # Step 4: Normalize
    X = normalizer.transform(feature_df)
    
    # Step 5: Predict
    predictions = model.predict(X)
    
    # Step 6: Output results
    for i, pred in enumerate(predictions):
        label = "FAULT" if pred == 1 else "NORMAL"
        print(f"Segment {i}: {label}")
    
    print("\nPrediction completed!")


# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    predict_fault()