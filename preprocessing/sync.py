# preprocessing/sync.py

import pandas as pd
import numpy as np
from config.config import *

# ==============================
# LOAD RAW DATA
# ==============================

def load_data():
    current = pd.read_csv("current.csv")
    voltage = pd.read_csv("voltage.csv")
    vibration = pd.read_csv("vibration.csv")
    temperature = pd.read_csv("temperature.csv")
    
    return current, voltage, vibration, temperature


# ==============================
# RESAMPLE FUNCTION
# ==============================

def resample_signal(df, target_length):
    """
    Resample signal to match target length using interpolation
    """
    x_old = np.linspace(0, 1, len(df))
    x_new = np.linspace(0, 1, target_length)
    
    y_new = np.interp(x_new, x_old, df.values)
    
    return y_new


# ==============================
# SYNCHRONIZATION FUNCTION
# ==============================

def synchronize():
    
    print("Synchronizing data...")
    
    current, voltage, vibration, temperature = load_data()
    
    # Choose reference signal (current)
    target_length = len(current)
    
    # Resample all signals to same length
    voltage_resampled = resample_signal(voltage["voltage"], target_length)
    vibration_resampled = resample_signal(vibration["vibration"], target_length)
    temp_resampled = resample_signal(temperature["temperature"], target_length)
    
    # Create unified dataframe
    synced_df = pd.DataFrame({
        "current": current["current"],
        "voltage": voltage_resampled,
        "vibration": vibration_resampled,
        "temperature": temp_resampled
    })
    
    print("Synchronization complete!")
    
    return synced_df


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    df = synchronize()
    print(df.head())