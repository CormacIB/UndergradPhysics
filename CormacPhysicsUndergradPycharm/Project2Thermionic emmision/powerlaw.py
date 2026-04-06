#%%
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from numpy.ma.extras import average
from sympy import transpose
from sympy.series.formal import Coeff
import matplotlib
from numpy import genfromtxt

# Data1
Voltage = np.array([29.857, 39.661, 49.926, 59.755, 19.853, 10.454, 6.275, 5.022,
                    4.087, 3.131, 2.544, 1.925, 1.005, 0.459, 0.317])
Current = np.array([0.14622, 0.14731, 0.1602, 0.16575, 0.15382, 0.1544, 0.1425, 0.14302,
                    0.14695, 0.14222, 0.11618, 0.11283, 0.09088, 0.05481, 0.04655])

#%%
# Data2
Voltage = np.array([30.378,
39.621,
49.994,
58.73,
20.47,
10.647,
6.364,
5.2143,
4.014,
3.311,
2.261,
1.123,
0.863,
0.701,
0.176])
Current = np.array([0.55366,
0.55601,
0.564304,
0.57007,
0.54855,
0.53429,
0.51332,
0.50054,
0.44691,
0.3694,
0.24733,
0.13069,
0.1078,
0.09455,
0.05645])

#%%
#Data 3
Voltage = np.array([0.7,
0.887,
1.195,
1.928,
3.09,
3.75,
4.364,
4.955,
5.617,
6.161,
9.941,
19.74,
29.894,
40.247,
60.289,])

Current = np.array([0.03563,
0.03964,
0.04398,
0.04756,
0.04978,
0.05041,
0.05093,
0.05148,
0.05212,
0.05259,
0.0537,
0.05532,
0.05635,
0.05733,
0.0585,])

#%%
my_data = genfromtxt('thermionic emission data test.csv', delimiter=',')

print(my_data)
Voltage = my_data[:,0]
Current = my_data[:,2]

print(Voltage)
print(Current)

#%%

#Plotting
#This gets rid of the empty entries in the voltage/current arrays
valid_indices = Voltage < 6
filtered_Voltage = Voltage[valid_indices]
filtered_Current = Current[valid_indices]
# Take logarithm of the filtered data
log_Voltage = np.log(filtered_Voltage)
log_Current = np.log(filtered_Current)

# Fit a linear regression in log-log space (log(y) = m * log(x) + c)
coeffs = np.polyfit(log_Voltage, log_Current, 1)
b = coeffs[0]  # Slope (power-law exponent)
a = np.exp(coeffs[1])  # Convert back from log space

print(f"Filtered power-law parameters: a = {a:.5f}, b = {b:.5f}")

# Generate fitted curve for plotting
t = np.linspace(min(filtered_Voltage), max(filtered_Voltage), 100)
fit_curve1 = a * t**b  # Power-law function



# Plot original data
plt.scatter(filtered_Voltage, filtered_Current, color='red', label="Filtered Data- Space-charge dependance (V < 6V)")  # Filtered points
plt.plot(t, fit_curve1, 'r-', label=f"Power Law Fit: {a:.5f} * x^{b:.5f}")

# Labels & Legend
plt.xlabel("Voltage (V)")
plt.ylabel("Current (mA)")
plt.title("Voltage vs. Current (Power-Law Fit for V < 6V)")
plt.legend()
plt.show()

#%%

#Trying to plot a linear fit to the data

Coeffs = np.polyfit(Voltage, Current, 1)
b = Coeffs[1] #Slope?
a = Coeffs[0] #Intercept?
t = np.linspace(min(Voltage), max(Voltage), 100)

print(f"Filtered power-law parameters: a = {a:.5f}, b = {b:.5f}")

fit_curve2 = a*t**b
plt.scatter(Voltage, Current)
plt.plot(t, fit_curve2, 'r-', label=f"Power Law Fit: {a:.5f} * x^{b:.5f}")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (mA)")
plt.title("Voltage vs. Current (Power-Law Fit for V < 6V)")
plt.legend()
plt.show()

#%%
