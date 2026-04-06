import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as pyplot
from numpy import genfromtxt

from main import my_data

#%%
my_data = genfromtxt('thermionic emission data(Sheet1).csv', delimiter=',')
Solenoid_Voltage = my_data[:,0]
Anode_Current = my_data[:,1]

Sv10 = np.zeros(len(my_data))
Sv25 = np.zeros(len(my_data))
Sv50 = np.zeros(len(my_data))
Sv100 = np.zeros(len(my_data))


x=0
while x < len(Solenoid_Voltage):
    Sv25[x] = Solenoid_Voltage[x]
    x = x + 1
    if Solenoid_Voltage[x-1] - Solenoid_Voltage[x] > 0.01:
        break

while x < len(Solenoid_Voltage):
    Sv10[x] = Solenoid_Voltage[x]
    x = x + 1
    if Solenoid_Voltage[x-1] - Solenoid_Voltage[x] > 0.01:
        break



print(Sv10)
print(Sv25)



#%%
plt.scatter(Solenoid_Voltage, Anode_Current)
plt.show()