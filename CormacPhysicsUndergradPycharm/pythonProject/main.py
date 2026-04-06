import math
from array import array
from fileinput import close

import matplotlib.pyplot as plt
import numpy as np

Dm = np.zeros((1851, 1851))
Data = np.zeros((1851, 20))

x1 = [1.1,0]
x2 = [0,1.4]

def distance(x1, x2):
    x3 = np.zeros(20)
    D = 0
    for i in range(20):
        x3[i] = x1[i]-x2[i]
        D += x3[i]*x3[i]
    D = np.sqrt(D)
    return D

def circleintx(d1,d2,ref1x):
    y = np.sqrt(np.abs(-((d1**2-d2**2+ref1x)/(2*ref1x))**2+d1**2))
    x = np.sqrt(np.abs(d1**2-y**2))
    return x
print(circleintx(np.sqrt(8),math.sqrt(5),1))

def circleinty(d1,d2,ref1x):
    y = np.sqrt(np.abs(-((d1**2-d2**2+ref1x)/(2*ref1x))**2+d1**2))
    x = np.sqrt(np.abs(d1**2-y**2))+100
    return y

f = open("secret_object_3.txt", "r") #Opens a file
for i in range(1851):
    line = f.readline()
    for val in range(20): #For each position in the line
        Data[i,val] = float(line.split()[val]) #Assigns each string to a spot in the array as a vector
f.close()

for j in range(1851):
    for i in range(1851):
        Dm[j,i] = distance(Data[j],Data[i])

#print(Dm[3,3])

ICx = np.array([0,Dm[0,1],circleintx(Dm[0,2],Dm[1,2],Dm[0,1])])
IXy = np.array([0,0,circleinty(Dm[0,2],Dm[1,2],Dm[0,1])])

Picx = np.zeros(1851)
Picy = np.zeros(1851)

Picx[0] = 0
Picx[1] = Dm[0,1]

for i in range(1849):
    Picx[i+2] = circleintx(Dm[0,i],Dm[1,i],Dm[0,1])
    Picy[i + 2] = circleinty(Dm[0, i], Dm[1, i], Dm[0, 1])

plt.plot(Picx,Picy, 'o')
plt.show()




