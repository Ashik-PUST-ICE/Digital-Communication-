import numpy as np
import matplotlib.pyplot as plt

# Generate random binary sequence

binary_sequence = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

N=len(binary_sequence)
print('The binary sequence is', binary_sequence)

# Generate time axis
t = np.linspace(0, N, N*100)  # Time axis with finer resolution

# Create Polar NRZ waveform
polar_nrz_waveform = []
for bit in binary_sequence:
    if bit == 0:
        polar_nrz_waveform.extend([-1]*100)  # Negative voltage for binary 0
    else:
        polar_nrz_waveform.extend([1]*100)  # Positive voltage for binary 1

# Plot the waveform
plt.figure(1)
plt.plot(t, polar_nrz_waveform, linewidth=2, color='red')  # Change color to differentiate from Unipolar NRZ
plt.ylim(-1.5, 1.5)  # Set y-axis limits
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Polar NRZ Signaling')
plt.grid(True)
plt.show()
