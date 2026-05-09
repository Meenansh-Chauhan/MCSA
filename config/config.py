# config/config.py

# Segmentation parameters
WINDOW_SIZE = 20
OVERLAP = 0.5  # 50% overlap for example

# Sampling Rates (Hz) - matching the generators in collect_data.py
SAMPLING_RATE_CURRENT = 1000
SAMPLING_RATE_VOLTAGE = 1000
SAMPLING_RATE_VIBRATION = 2000
SAMPLING_RATE_TEMPERATURE = 10

# Filtering Parameters (Bandpass cutoffs)
LOWCUT_CURRENT = 45.0
HIGHCUT_CURRENT = 55.0
LOWCUT_VIBRATION = 10.0
HIGHCUT_VIBRATION = 1000.0

# Feature Engineering
NUM_FFT_PEAKS = 5