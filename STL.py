import numpy as np
from statsmodels.tsa.seasonal import STL
from scipy.fft import fft

# Simulated time series data
# Replace this with your own time series data
time_series_data = np.sin(np.linspace(0, 2 * np.pi, 100) * 2)  # Example sine wave

# Perform STL decomposition
stl = STL(time_series_data, seasonal=13)  # Adjust the seasonal parameter as needed
result = stl.fit()

# Extract seasonal component
seasonal_component = result.seasonal

# Compute the Fourier transform to get frequency components
seasonal_fft = fft(seasonal_component)

# Extract the phase (angle) of the dominant frequency component
dominant_frequency_phase = np.angle(seasonal_fft[1])

print("Phase of dominant frequency component:", dominant_frequency_phase)
