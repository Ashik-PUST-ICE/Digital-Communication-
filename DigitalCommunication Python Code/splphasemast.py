import numpy as np
import matplotlib.pyplot as plt

# Function to convert spaced input to unspaced input
def remove_spaces(input_string):
    return ''.join(input_string.split())

# Function to get binary input from the user
def get_binary_input():
    binary_sequence = input("Enter the binary sequence (0 or 1 for each bit): ")
    binary_sequence = remove_spaces(binary_sequence)  # Remove spaces
    return [int(bit) for bit in binary_sequence]  # Convert to list of integers

# Get binary input from the user
n = get_binary_input()
N = len(n)

# Binary to Manchester Conversion
nnn = []
for bit in n:
    if bit == 1:
        nn = [1, -1]
    else:
        nn = [-1, 1]
    nnn.extend(nn)

# Manchester Coding Pulse Shaping
i = 0
l = 0.5
t = np.arange(0, N + 0.01, 0.01)
y = []
for j in range(len(t)):
    if t[j] <= l:  # Condition for the first half cycle
        y.append(nnn[i])  # Assign values for the first half cycle
    else:
        y.append(nnn[i])
        i += 1
        l += 0.5

plt.plot(t, y, linewidth=2)  # Linewidth 2 for clear visualization
plt.axis([0, N, -1.5, 1.5])  # Axis set-up
plt.grid(True)
plt.title("Manchester Coding")
plt.show()
