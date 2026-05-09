# feature_engineering/fusion.py

import pandas as pd

from feature_engineering.statistical_features import extract_all_stat_features
from feature_engineering.fft_features import extract_all_fft_features

# ==============================
# FEATURE FUSION FUNCTION
# ==============================

def extract_features_from_segment(segment):
    
    # Statistical features
    stat_features = extract_all_stat_features(segment)
    
    # FFT features
    fft_features = extract_all_fft_features(segment)
    
    # Combine both
    combined_features = {**stat_features, **fft_features}
    
    return combined_features


# ==============================
# APPLY TO ALL SEGMENTS
# ==============================

def build_feature_dataframe(segments):
    
    print("Building feature dataset...")
    
    feature_list = []
    
    for i, segment in enumerate(segments):
        
        features = extract_features_from_segment(segment)
        
        feature_list.append(features)
    
    df_features = pd.DataFrame(feature_list)
    
    print("Feature dataset created!")
    
    return df_features


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    
    from preprocessing.segmentation import segment_signal
    from preprocessing.sync import synchronize
    from preprocessing.filtering import filter_signals
    
    print("Testing feature fusion...\n")
    
    df = synchronize()
    df = filter_signals(df)
    segments = segment_signal(df)
    
    feature_df = build_feature_dataframe(segments)
    
    print("\nFeature DataFrame:\n")
    print(feature_df.head())
    
    print("\nTotal Features:", feature_df.shape[1])