import numpy as np
import matplotlib.pyplot as plt
import math

t = 250000
pos = np.zeros((t,2))
GM = 1
pos[0,0] = 50
pos[1,0] = 50
dt = .01
l= 3.5



for i in range(1, t-1):
    #l = pos[i, 0]**2 * (pos[i+1,1]-pos[i,1]) / dt
    pos[i+1,0] = 2*pos[i,0] - pos[i-1,0] + dt**2 * (-GM/(pos[i,0]**2) + l**2/pos[i,0]**3 - 3*GM*l**2/pos[i,0]**4)
    pos[i+1,1] = pos[i,1] + dt * l / ((0.5*(pos[i+1,0]+pos[i,0]))**2)

    if pos[i+1,0] < 2*GM:
        print("black hole time yay")
        break


# Convert polar to Cartesian
x = pos[:,0] * np.cos(pos[:,1])
y = pos[:,0] * np.sin(pos[:,1])

# Plot trajectory
plt.figure(figsize=(6,6))
plt.plot(x, y, label="Orbit trajectory")
plt.plot(0, 0, 'yo', label="Central mass")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")  # keep aspect ratio square
plt.title("Orbit Simulation")
plt.show()

print(pos)
