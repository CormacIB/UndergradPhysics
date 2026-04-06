#%%
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from networkx.algorithms.bipartite import projection
from networkx.algorithms.bipartite.basic import color
from networkx.algorithms.operators.binary import difference
from numpy.ma.extras import average
from sympy import transpose
from sympy.plotting import plot3d
from sympy.series.formal import Coeff
import matplotlib

#%%
# Problem 5.5

def leastsquaresATA(Subspace, Vector):
    AT = numpy.transpose(Subspace)
    ATA = numpy.matmul(AT, Subspace)
    AY = numpy.dot(AT, Vector)
    return numpy.linalg.solve(ATA, AY)

def leastsqauresconstrained(Subspace, Vector):
    AT = numpy.transpose(Subspace)

def leastsquareserror(Projection, Vector):
    return  np.sqrt(numpy.linalg.norm(Projection - Vector))

def laGrangeP(Points, t):
    Lk = 0
    L = 1
    for j in range(len(Points)):
        for i in range(len(Points)):
            if Points[i] != Points[j]:
                L = L*(t-Points[j])/(Points[j]-Points[i])
        Lk = Lk + L*Points[j]
    return Lk

#Part A)
year = np.array([1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995])
amount = np.array([86, 99.8, 115.8, 125, 132.6, 143.1, 156.3, 169.5])
A = numpy.ones((8,2))

for i in range(len(year)):
    A[i][1] = year[i]

Coeff = leastsquaresATA(A, amount)

x = np.linspace(1955, 2000, 100)
plt.scatter(year,amount)
plt.plot(x, Coeff[0]+Coeff[1]*x)
plt.xlabel('Year')
plt.ylabel('Amount of waste in millions of Tons')
plt.show()

Projection = Coeff[0] + Coeff[1]*year
print(Projection)
print(leastsquareserror(Projection, amount))

# Part B)
print(Coeff[0]+Coeff[1]*2000, Coeff[0]+Coeff[1]*2005) # Gives our estimate in 2000 and year 2005


#%%
# Part C)
amountlog = np.zeros(8)
for i in range(len(amount)):
    amountlog[i] = np.log(amount[i])
Coeff = leastsquaresATA(A, amountlog)

x = np.linspace(1950, 2000, 100)
plt.scatter(year,amount)
plt.plot(x, np.exp(Coeff[0])*np.exp(Coeff[1]*x))
plt.xlabel('Year')
plt.ylabel('Amount (Best fine line exponential)')
plt.show()

Projection = np.exp(Coeff[0])*np.exp(Coeff[1]*year)
leastsquareserror(Projection, amount)

#In conclusion: I like the linear fit over the exponential because it has a smaller average error :)
#%%
#Problem 5.5.9
x = np.array([1,1,2,2,3,3])
y = np.array([1,2,1,2,2,4])
z = np.array([3,6,11,-2,0,3])


A = np.ones((6,3))
for i in range(len(x)):
    A[i][1] = x[i]
    A[i][2] = y[i]

Coeff = leastsquaresATA(A, z)
print(Coeff)

U = np.linspace(0,5,10)
W = np.linspace(0,5,10)
X, Y = np.meshgrid(U,W)
Z = Coeff[0]+Coeff[1]*X+Coeff[2]*Y
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,Z, alpha = .5, color = 'green')
ax.scatter(x,y,z)
plt.xlabel('X')
plt.ylabel('Y')
#ax.view_init(45, 30,10)
plt.show()

Projection = Coeff[0]+Coeff[1]*x+Coeff[2]*y
leastsquareserror(Projection, z)


#%%
x = np.array([1,1,2,2,3,3])
y = np.array([1,2,1,2,2,4])
z = np.array([3,6,11,-2,0,3])


A = np.ones((6,3))
for i in range(len(x)):
    A[i][1] = x[i]
    A[i][2] = y[i]

Coeff = leastsquaresATA(A, z)
print(Coeff)
x = np.array([1,1,2,2,3,3,2])
y = np.array([1,2,1,2,2,4,2])
z = np.array([3,6,11,-2,0,3,0])

U = np.linspace(0,5,10)
W = np.linspace(0,5,10)
X, Y = np.meshgrid(U,W)
Z = Coeff[1]*X-Coeff[2]*X
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,Z, alpha = .5, color = 'green')
ax.scatter(x,y,z)
plt.xlabel('X')
plt.ylabel('Y')
#ax.view_init(45, 0,45)
plt.show()




#%%
#Problem 5.19

x = np.array([1,2,4,6,8,10])
y = np.array([3,3,4,6,7,8])
#A) Find the Least squares solution to the data

A = np.ones((6,2))
for i in range(len(x)):
    A[i][1] = x[i]

Coeff = leastsquaresATA(A, y)
print(Coeff)

t = np.linspace(0,11,100)
plt.scatter(x,y)
plt.plot(t,Coeff[0]+Coeff[1]*t)
plt.show()

#C) Find the polynomial solution to the data

#%%
t= np.linspace(0,11,100)
A = np.ones((6,3))
for i in range(len(x)):
    A[i][1] = x[i]
    A[i][2] = x[i]**2

Coeff = leastsquaresATA(A, y)
plt.scatter(x,y)
plt.plot(t,Coeff[0]+Coeff[1]*t+Coeff[2]*t**2)
plt.show()
print(Coeff)

#%%
#Find the interpolating polynomial to the data
t = np.linspace(0,11,100)
A = np.ones((6,6))
for i in range(len(x)):
    A[i][1] = x[i]
    A[i][2] = x[i]**2
    A[i][3] = x[i]**3
    A[i][4] = x[i]**4
    A[i][5] = x[i]**5

Coeff = leastsquaresATA(A, y)
plt.scatter(x,y)
plt.plot(t,Coeff[0]+Coeff[1]*t+Coeff[2]*t**2+Coeff[3]*t**3+Coeff[4]*t**4+Coeff[5]*t**5)
#plt.plot(t, laGrangeP(y,t))
plt.ylim(0,11)
plt.show()



