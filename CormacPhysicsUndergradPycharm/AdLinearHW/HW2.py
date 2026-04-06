#%%
import matplotlib
import matplotlib.pyplot as plt
import  numpy
import numpy as np
from sympy.codegen import Print

from main import Coeff, leastsquareserror


def leastsquaresATA(Subspace, Vector):
    AT = numpy.transpose(Subspace)
    ATA = numpy.matmul(AT, Subspace)
    AY = numpy.dot(AT, Vector)
    return numpy.linalg.solve(ATA, AY)


#%%
#Problem 5.44 a) - Approximate t^2 using rcos(t+d) using 5 and 9 equally spaced sample points on 0-pi
p5 = [0,1/4*np.pi,1/2*np.pi,3/4*np.pi,np.pi]
p9 = np.zeros(9)
for i in range(len(p9)):
    p9[i] = np.pi*i/8

t5 = np.zeros(5) #Make the sample vector for 5 points
for i in range(len(p5)):
    t5[i] = p5[i]**2
A = np.zeros((5,2))
for i in range(len(A)): #Make our function matrix 5 pts
    A[i][0] = np.cos(p5[i])
    A[i][1] = np.sin(p5[i])
Coeff5 = leastsquaresATA(A,t5)
print(Coeff5)

t9 = np.zeros(9) #make the sample vector for 9 points
for i in range(len(p9)):
    t9[i] = p9[i]**2
A9 = np.zeros((9,2))
for i in range(len(A)): #Make our function matrix 9 pts
    A9[i][0] = np.cos(p9[i])
    A9[i][1] = np.sin(p9[i])
Coeff9 = leastsquaresATA(A9,t9)

fi, ax = plt.subplots(1,2)
n = np.linspace(0,5,100)
ax[0].scatter(p5,t5)
ax[0].plot(n,Coeff5[0]*np.cos(n)+Coeff5[1]*np.sin(n))
ax[1].scatter(p9,t9)
ax[1].plot(n,Coeff9[0]*np.cos(n)+Coeff9[0]*np.sin(n))
plt.show()

#%% #Part B) What can we do with an extra rcos(d+1)?
# We can re-use the samples that we've already initialized, but we need new A matracis

B5 = np.zeros((5,4))
for i in range(len(B5)):
    B5[i][0] = np.cos(p5[i])
    B5[i][1] = np.sin(p5[i])
    B5[i][2] = np.cos(2*p5[i])
    B5[i][3] = np.sin(2*p5[i])
Coeff5 = leastsquaresATA(B5,t5)
print(B5)

B9 = np.array(np.transpose([np.cos(p9),np.sin(p9),np.cos(2*p9),np.sin(2*p9)]))
#for i in range(len(B9)):
    #B9[i][0] = np.cos(p9[i])
    #B9[i][1] = np.sin(p9[i])
    #B9[i][2] = np.cos(2*p9[i])
    #B9[i][3] = np.sin(2*p9[i])
Coeff9 = leastsquaresATA(B9,t9)
print(B9)

fig, ax = plt.subplots(1,2)
n = np.linspace(0,5,100)
ax[0].scatter(p5,t5)
ax[0].plot(n,Coeff5[0]*np.cos(n)+Coeff5[1]*np.sin(n)+Coeff5[2]*np.cos(2*n)+Coeff5[3]*np.sin(3*n))
ax[1].scatter(p9,t9)
ax[1].plot(n,Coeff9[0]*np.cos(n)+Coeff9[1]*np.sin(n)+Coeff9[2]*np.cos(2*n)+Coeff9[3]*np.sin(3*n))
plt.show()

#%%Problem 5.45
#Define our function, sample, interval
def sampleY(numberSamplePoints):
    A = np.zeros((numberSamplePoints-1))
    B = np.zeros((numberSamplePoints-1))
    for i in range(numberSamplePoints-1):
        A[i] = -np.pi+2*np.pi*i/(numberSamplePoints)
        B[i] = 1/(1+A[i]**2)
    return B

def sampleX(numberSamplePoints):
    A = np.zeros((numberSamplePoints-1))
    for i in range(numberSamplePoints-1):
        A[i] = -np.pi+2*np.pi*i/(numberSamplePoints)
    return A

ax = sampleX(4)
ay = sampleY(4)
bx = sampleX(8)
by = sampleY(8)
cx = sampleX(16)
cy = sampleY(16)
dx = sampleX(16)
dy = sampleY(16)
onesA = np.ones(len(ax))
onesB = np.ones(len(bx))
onesC = np.ones(len(cx))
onesD = np.ones(len(dx))
A = np.array(np.transpose([onesA,np.cos(ax),np.sin(ax)]))
B = np.array(np.transpose([onesB,np.cos(bx),np.sin(bx),np.cos(2*bx),np.sin(2*bx)]))
C = np.array(np.transpose([onesC,np.cos(cx),np.sin(cx),np.cos(2*cx),np.sin(2*cx)]))
D = np.array(np.transpose([onesD,np.cos(dx),np.sin(dx),np.cos(2*dx),np.sin(2*dx), np.cos(3*dx),np.sin(3*dx)]))
CoeffA=leastsquaresATA(A,ay)
CoeffB=leastsquaresATA(B,by)
CoeffC=leastsquaresATA(C,cy)
CoeffD=leastsquaresATA(D,dy)



fig, ax = plt.subplots(2,2)
n = np.linspace(-5,5,100)
ax[0][0].scatter(sampleX(4),sampleY(4))
ax[0][1].scatter(sampleX(8),sampleY(8))
ax[1][0].scatter(sampleX(16),sampleY(16))
ax[1][1].scatter(sampleX(16),sampleY(16))
ax[0][0].plot(n,CoeffA[0]+CoeffA[1]*np.cos(n)+CoeffA[2]*np.sin(n))
ax[0][1].plot(n,CoeffB[0]+CoeffB[1]*np.cos(n)+CoeffB[2]*np.sin(n)+CoeffB[3]*np.cos(2*n)+CoeffB[4]*np.sin(2*n))
ax[1][0].plot(n,CoeffC[0]+CoeffC[1]*np.cos(n)+CoeffC[2]*np.sin(n)+CoeffC[3]*np.cos(2*n)+CoeffC[4]*np.sin(2*n))
ax[1][1].plot(n,CoeffD[0]+CoeffD[1]*np.cos(n)+CoeffD[2]*np.sin(n)+CoeffD[3]*np.cos(2*n)+CoeffD[4]*np.sin(2*n)+CoeffD[5]*np.cos(3*n)+CoeffD[6]*np.sin(3*n))

for i in range(2):
    for j in range(2):
        ax[i][j].set_xlim(-4,4)
        ax[i][j].set_ylim(-2,2)
plt.show()







