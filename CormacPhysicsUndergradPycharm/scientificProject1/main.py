#%%
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
#%%
# Defining data for the dataframe
my_data = genfromtxt('/Users/cormacbillick/PycharmProjects/scientificProject1/Book 14(Sheet1) (1).csv', delimiter=',')

print(my_data)
Counts = my_data[:,0]
Velocity = my_data[:,2]
Something = np.zeros(len(Velocity))
for i in range(len(Velocity)):
    Something[i] = Velocity[i]*632.8/2/80/9625
#%%

plt.scatter(Counts, Something)
plt.show()
