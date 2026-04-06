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

#%%
# Problem 5.5


#Part A)
year = np.array([1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995])
amount = np.array([86, 99.8, 115.8, 125, 132.6, 143.1, 156.3, 169.5])
A = numpy.ones((8,2))

for i in range(len(year)):
    A[i][1] = year[i]


def leastsquaresATA(Subspace, Vector):
    AT = numpy.transpose(Subspace)
    ATA = numpy.matmul(AT, Subspace)
    AY = numpy.dot(AT, Vector)
    return numpy.linalg.solve(ATA, AY)

Coeff = leastsquaresATA(A, amount)

e = np.zeros(8)
for i in range(len(amount)):
    e[i] = np.abs(Coeff[0]+Coeff[1]*year[i] - amount[i])

print(average(e))


x = np.linspace(1955, 2000, 100)
plt.scatter(year,amount)
plt.plot(x, Coeff[0]+Coeff[1]*x)
plt.xlabel('Year')
plt.ylabel('Amount of waste in millions of Tons')
plt.show()

#print(Coeff)




# Part B)
print(Coeff[0]+Coeff[1]*2000, Coeff[0]+Coeff[1]*2005) # Gives our estimate in 2000 and year 2005


#%%
# Part C)
amountlog = np.zeros(8)
for i in range(len(amount)):
    amountlog[i] = np.log(amount[i])
Coeff = leastsquaresATA(A, amountlog)
C = .00000000000001

x = np.linspace(1950, 2000, 100)
plt.scatter(year,amount)
plt.plot(x, C*np.exp(Coeff[1]*x))
plt.xlabel('Year')
plt.ylabel('Amount (Best fine line exponential)')
plt.show()