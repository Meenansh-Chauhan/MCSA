# preprocessing/filtering.py

import numpy as np
from scipy.signal import butter, filtfilt
from config.config import *

# ==============================
# FILTER DESIGN
# ==============================

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    
    b, a = butter(order, [low, high], btype='band')
    return b, a


# ==============================
# APPLY BANDPASS FILTER
# ==============================

def apply_bandpass_filter(signal, lowcut, highcut, fs):
    b, a = butter_bandpass(lowcut, highcut, fs)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal


# ==============================
# APPLY ALL FILTERS
# ==============================

def filter_signals(df):
    
    print("Filtering signals...")
    
    # Current
    df["current"] = apply_bandpass_filter(
        df["current"],
        LOWCUT_CURRENT,
        HIGHCUT_CURRENT,
        SAMPLING_RATE_CURRENT
    )
    
    # Voltage
    df["voltage"] = apply_bandpass_filter(
        df["voltage"],
        20,
        450,
        SAMPLING_RATE_VOLTAGE
    )
    
    # Vibration
    df["vibration"] = apply_bandpass_filter(
        df["vibration"],
        LOWCUT_VIBRATION,
        HIGHCUT_VIBRATION,
        SAMPLING_RATE_VIBRATION
    )
    
    # Temperature (simple smoothing)
    df["temperature"] = df["temperature"].rolling(window=3, min_periods=1).mean()
    
    print("Filtering complete!")
    
    return df


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    
    print("Starting filtering test...\n")
    
    from preprocessing.sync import synchronize
    
    df = synchronize()
    print("\nAfter synchronization:\n", df.head())
    
    df_filtered = filter_signals(df)
    print("\nAfter filtering:\n", df_filtered.head())
    
    print("\nFiltering test completed successfully!")