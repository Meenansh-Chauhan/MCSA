# preprocessing/segmentation.py

import numpy as np
from config.config import *

# ==============================
# SEGMENTATION FUNCTION
# ==============================

def segment_signal(df):
    
    print("Segmenting signal...")
    
    window_samples = int(WINDOW_SIZE * SAMPLING_RATE_CURRENT)
    step_size = int(window_samples * (1 - OVERLAP))
    
    segments = []
    
    for start in range(0, len(df) - window_samples + 1, step_size):
        end = start + window_samples
        
        segment = df.iloc[start:end]
        segments.append(segment)
    
    print(f"Total segments created: {len(segments)}")
    
    return segments


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    
    from preprocessing.sync import synchronize
    from preprocessing.filtering import filter_signals
    
    print("Starting segmentation test...\n")
    
    df = synchronize()
    df = filter_signals(df)
    
    segments = segment_signal(df)
    
    print("\nFirst segment preview:\n")
    print(segments[0].head())
    
    print("\nSegmentation completed successfully!")