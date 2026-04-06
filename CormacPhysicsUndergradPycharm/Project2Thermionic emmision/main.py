#%%
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import genfromtxt

#%%
# Defining data for the dataframe

my_data = genfromtxt('/Users/cormacbillick/PycharmProjects/Project2Thermionic emmision/thermionic emission data(Sheet1).csv', delimiter=',')

Voltage = np.empty(15)
Current = np.empty(15)
for i in range(15):
    Voltage[i] = my_data[i][0]
    Current[i] = my_data[i][1]
# Creating the dataframe
#print(my_data)
print(Voltage)
print(Current)
#%%

plt.scatter(my_data[:,0], my_data[:2])
plt.show()
