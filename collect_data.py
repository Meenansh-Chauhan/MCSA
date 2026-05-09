# collect_data.py

import numpy as np 
import pandas as pd
from config.config import *

# ==============================
# SIGNAL GENERATORS (SIMULATION)
# ==============================

def generate_current_signal(duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    
    signal = (
        10 * np.sin(2 * np.pi * 50 * t) + 
        2 * np.sin(2 * np.pi * 150 * t) + 
        np.random.normal(0, 0.5, len(t))
    )
    
    return t, signal


def generate_voltage_signal(duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    
    signal = (
        220 * np.sin(2 * np.pi * 50 * t) +
        np.random.normal(0, 2, len(t))
    )
    
    return t, signal


def generate_vibration_signal(duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    
    signal = (
        0.5 * np.sin(2 * np.pi * 200 * t) +
        0.2 * np.sin(2 * np.pi * 800 * t) +
        np.random.normal(0, 0.2, len(t))
    )
    
    return t, signal


def generate_temperature_signal(duration, sampling_rate):
    num_samples = int(duration * sampling_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    signal = 30 + 0.1 * np.arange(num_samples) + np.random.normal(0, 0.2, num_samples)
    
    return t, signal


# ==============================
# DATA COLLECTION FUNCTION
# ==============================

def collect_data(duration=WINDOW_SIZE):
    
    print("Collecting data...")
    
    t_current, current = generate_current_signal(duration, SAMPLING_RATE_CURRENT)
    t_voltage, voltage = generate_voltage_signal(duration, SAMPLING_RATE_VOLTAGE)
    t_vibration, vibration = generate_vibration_signal(duration, SAMPLING_RATE_VIBRATION)
    t_temp, temperature = generate_temperature_signal(duration, SAMPLING_RATE_TEMPERATURE)
    
    # Save files in same folder (simple for now)
    pd.DataFrame({
        "time": t_current,
        "current": current
    }).to_csv("current.csv", index=False)
    
    pd.DataFrame({
        "time": t_voltage,
        "voltage": voltage
    }).to_csv("voltage.csv", index=False)
    
    pd.DataFrame({
        "time": t_vibration,
        "vibration": vibration
    }).to_csv("vibration.csv", index=False)
    
    pd.DataFrame({
        "time": t_temp,
        "temperature": temperature
    }).to_csv("temperature.csv", index=False)
    
    print("Data saved successfully!")


# ==============================
# RUN FILE
# ==============================

if __name__ == "__main__":
    collect_data(duration=20)