# feature_engineering/statistical_features.py

import numpy as np

# ==============================
# BASIC STAT FEATURES
# ==============================

def extract_stat_features(signal):
    
    features = {}
    
    mean = np.mean(signal)
    std = np.std(signal)
    
    features["mean"] = mean
    features["std"] = std
    features["rms"] = np.sqrt(np.mean(signal**2))
    features["max"] = np.max(signal)
    features["min"] = np.min(signal)
    
    # Avoid division by zero
    if std == 0:
        features["kurtosis"] = 0
        features["skewness"] = 0
    else:
        features["kurtosis"] = np.mean((signal - mean)**4) / (std**4)
        features["skewness"] = np.mean((signal - mean)**3) / (std**3)
    
    return features


# ==============================
# APPLY TO SEGMENT
# ==============================

def extract_all_stat_features(segment):
    
    all_features = {}
    
    for column in segment.columns:
        signal = segment[column].values
        
        stats = extract_stat_features(signal)
        
        for key, value in stats.items():
            all_features[f"{column}_{key}"] = value
    
    return all_features


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    
    from preprocessing.segmentation import segment_signal
    from preprocessing.sync import synchronize
    from preprocessing.filtering import filter_signals
    
    print("Testing statistical features...\n")
    
    df = synchronize()
    df = filter_signals(df)
    segments = segment_signal(df)
    
    features = extract_all_stat_features(segments[0])
    
    for k, v in features.items():
        print(f"{k}: {v}")