# feature_engineering/fft_features.py

import numpy as np
from config.config import *

# ==============================
# FFT FEATURE EXTRACTION
# ==============================

def extract_fft_features(signal, sampling_rate):
    
    features = {}
    
    # FFT
    fft_vals = np.fft.fft(signal)
    fft_vals = np.abs(fft_vals)
    
    freqs = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    
    # Take only positive frequencies
    positive_freqs = freqs[:len(freqs)//2]
    positive_fft = fft_vals[:len(fft_vals)//2]
    
    # Get top peaks
    peak_indices = np.argsort(positive_fft)[-NUM_FFT_PEAKS:]
    
    peak_freqs = positive_freqs[peak_indices]
    peak_magnitudes = positive_fft[peak_indices]
    
    # Store features
    for i in range(NUM_FFT_PEAKS):
        features[f"peak_freq_{i}"] = peak_freqs[i]
        features[f"peak_mag_{i}"] = peak_magnitudes[i]
    
    return features


# ==============================
# APPLY TO FULL SEGMENT
# ==============================

def extract_all_fft_features(segment):
    
    all_features = {}
    
    # Apply only to signals where FFT matters
    sensor_config = {
        "current": SAMPLING_RATE_CURRENT,
        "vibration": SAMPLING_RATE_VIBRATION,
        "voltage": SAMPLING_RATE_VOLTAGE
    }
    
    for column, fs in sensor_config.items():
        
        signal = segment[column].values
        
        fft_features = extract_fft_features(signal, fs)
        
        for key, value in fft_features.items():
            all_features[f"{column}_{key}"] = value
    
    return all_features


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    
    from preprocessing.segmentation import segment_signal
    from preprocessing.sync import synchronize
    from preprocessing.filtering import filter_signals
    
    print("Testing FFT feature extraction...\n")
    
    df = synchronize()
    df = filter_signals(df)
    segments = segment_signal(df)
    
    fft_features = extract_all_fft_features(segments[0])
    
    print("\nExtracted FFT Features:\n")
    for k, v in fft_features.items():
        print(f"{k}: {v}")