# Motor Current Signature Analysis (MCSA) Anomaly Detection

## Overview

This project is a complete pipeline for **Motor Current Signature Analysis (MCSA)**. It simulates the generation of multi-modal sensor signals (current, voltage, vibration, and temperature), applies signal processing techniques, extracts statistical and Fast Fourier Transform (FFT) features, and utilizes machine learning models to classify the state of the motor (NORMAL vs FAULT).

The repository demonstrates a scalable architecture for industrial predictive maintenance, incorporating data synchronization, filtering, feature engineering, and modeling.

## Project Structure

```text
├── collect_data.py               # Generates simulated sensor data (current, voltage, vibration, temperature)
├── config/
│   └── config.py                 # Configuration parameters for sampling rates, filtering, and segmentation
├── data/                         # Directory for storing external datasets
├── feature_engineering/
│   ├── fft_features.py           # Frequency-domain feature extraction using FFT
│   ├── statistical_features.py   # Time-domain statistical feature extraction
│   └── fusion.py                 # Combines features for model input
├── models/
│   ├── train.py                  # Model training pipeline
│   └── predict.py                # Prediction pipeline for anomaly detection
├── notebooks/                    # Jupyter notebooks for exploratory data analysis and visualization
├── preprocessing/
│   ├── filtering.py              # Bandpass filters to remove noise from signals
│   ├── normalization.py          # Feature scaling and normalization
│   ├── segmentation.py           # Signal segmentation and overlapping
│   └── sync.py                   # Time synchronization across different sensor modalities
├── src/                          # Additional helper scripts and utilities
└── venv/                         # Python virtual environment (ignored in git)
```


**Environment Management**: The project utilizes a virtual environment (`venv`) to isolate dependencies, preventing conflicts and maintaining a secure execution environment.

## Getting Started

### 1. Prerequisites

Ensure you have Python 3.8+ installed. 

### 2. Installation

Clone the repository and set up a virtual environment:

```bash
# Clone the repository
git clone <your-github-repo-url>
cd MCSA

# Activate the existing virtual environment (Windows)
.\venv\Scripts\activate
# For Linux/Mac: source venv/bin/activate

# Install dependencies (if you have a requirements.txt)
# pip install -r requirements.txt
```

### 3. Usage

**Step 1: Data Collection**  
Generate the simulated sensor data (Current, Voltage, Vibration, Temperature).
```bash
python collect_data.py
```

**Step 2: Prediction Pipeline**  
Run the end-to-end pipeline to preprocess data, extract features, and predict motor faults.
```bash
python models/predict.py
```

## Features

- **Multi-Sensor Simulation**: Generates realistic simulated data with adjustable parameters.
- **Advanced Signal Processing**: Applies bandpass filtering and robust signal segmentation.
- **Comprehensive Feature Engineering**: Extracts meaningful time-domain and frequency-domain characteristics.
- **Scalable Architecture**: Modular design allowing easy integration of new sensors or machine learning models.
