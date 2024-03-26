import numpy as np
import matplotlib.pyplot as plt

# Input binary sequence from the user
binary_sequence = input("Enter the binary sequence without spaces (e.g., 010101): ")

# Convert input string to list of integers
binary_sequence = [int(bit) for bit in binary_sequence.split()]

# Define the number of bits
N = len(binary_sequence)

print('The binary sequence is', binary_sequence)

# Generate time axis
t = np.linspace(0, N, N*100)  # Time axis with finer resolution

# Create Unipolar NRZ waveform
unipolar_nrz_waveform = np.repeat(binary_sequence, 100)  # Repeat each bit 100 times

# Plot the waveform
plt.figure(1)
plt.plot(t, unipolar_nrz_waveform, linewidth=2)
plt.ylim(-1.5, 1.5)  # Set y-axis limits
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Unipolar NRZ Signaling')
plt.grid(True)
plt.show()
