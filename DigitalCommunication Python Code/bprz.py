import numpy as np
import matplotlib.pyplot as plt

# Input binary sequence from the user
binary_sequence = input("Enter the binary sequence without spaces (e.g., 010101): ")

# Convert input string to list of integers
binary_sequence = [int(bit) for bit in binary_sequence.split()]

# Define the number of bits
N = len(binary_sequence)

print('The binary sequence is', binary_sequence)

# Convert binary sequence to bipolar sequence
bipolar_sequence = []
flag = True
for bit in binary_sequence:
    if bit == 1:
        if flag:
            bipolar_sequence.append(1)
        else:
            bipolar_sequence.append(-1)
        flag ^= True
    else:
        bipolar_sequence.append(0)

# Signal shaping
i = 1
a = 0
t = np.arange(0, N + 0.01, 0.01)
y = np.zeros(len(t))

for j in range(len(t)):
    if t[j] >= a and t[j] <= a + 0.5:
        y[j] = bipolar_sequence[i-1]
    elif t[j] >= a + 0.5 and t[j] <= i:
        pass
    else:
        a += 1
        i += 1

plt.plot(t, y, linewidth=2)
plt.grid(True)
plt.axis([0, N, -1.5, 1.5])
plt.title("Bipolar Return to Zero")
plt.show()
