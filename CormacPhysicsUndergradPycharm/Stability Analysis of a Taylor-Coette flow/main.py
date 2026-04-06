import matplotlib.pyplot as plt
import numpy as np

a1 = .25
omega = 1
a2 = 2

r = np.linspace(a1, a2, 100)

uphi = -omega*a1**2*r/(a2**2-a1**2)    +   omega*a1**2*a2**2/((a2**2-a1**2)*r)

x_values = [a1, a2]  # actaul values here
for x_val in x_values:
    plt.axvline(x=x_val, color='r', linestyle='dotted', linewidth=1)

y_marker = a1*omega  # put desired y here
plt.scatter(0, y_marker, color='blue', s=50, label=f'Marker at a1*Omega')

plt.plot(r, uphi)
plt.axhline(y=0, color='black', linewidth=1)  # X-axis
plt.axvline(x=0, color='black', linewidth=1)  # Y-axis
plt.xlabel('Radius')
plt.ylabel('Velocity (phi)')
plt.legend()

plt.show()