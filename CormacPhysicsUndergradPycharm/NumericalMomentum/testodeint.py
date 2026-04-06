import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def diffx(n, x, lam):  # Differential equation in x
    u, v = n
    dudx = v
    dduddx = u * lam
    return [dudx, dduddx]

def difft(t, y, lam, D):  # Differential equation in t
    dydt = -D * lam * t
    return [dydt]

# Parameters
lam = -1
D = .8
x0 = [0, 1]  # Initial values for u and v
t0 = [0]     # Initial value for y
x = np.linspace(0, 1, 500)
t = np.linspace(0, 1, 500)

# Solving the differential equations
solx = odeint(diffx, x0, x, args=(lam,))
solt = odeint(difft, t0, t, args=(lam, D))

# Plotting the solution
plt.plot(x, solx[:, 0] * solt[:, 0], 'r', label='u(x)*y(t)')

plt.legend(loc='best')
plt.xlabel('x')
plt.grid()
plt.show()
