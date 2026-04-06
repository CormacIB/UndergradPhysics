import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint



# Create a grid of points
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)



# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([0, 5])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Vector Field')

# Initial vector field
U = Y  # x-component of the vector field
V = 0   # y-component of the vector field

norm = abs(U**2 + V**2)**0.5

quiver = ax.quiver(X, Y, U, V, norm, cmap = "viridis")

# Function to update the vector field for each frame of the animation
def update(frame):
    t = frame / 10  # Time variable for animation
    U = 2*t*Y  # x-component changes with time
    V = 0  # y-component changes with time
    quiver.set_UVC(U, V)  # Update the quiver plot
    return quiver,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

# Show the animation
plt.show()

#Simulating 2-d Navier stokes for an incompressible flow- initial conditions, velocity in the x direction to be constant
#velocity in the y direction to be 0