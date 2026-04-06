import numpy as np
import matplotlib.pyplot as plt

# Define cylinder radii and rotation speed
r_i = 1   # Inner cylinder radius
r_o = 4   # Outer cylinder radius
Omega_1 = 1  # Rotation speed of inner cylinder

# Define grid
x = np.linspace(-5, 5, 40)
y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(x, y)

#Trig conversion
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# A and B when Omega_2 = 0
A = (Omega_1  * r_o**2) / (r_o**2 - r_i**2)
B = (-Omega_1 * r_o **2 * r_i**2) / (r_o**2 - r_i**2)

#Velocity field definition
V_theta = A * R + B / R
Vx = -V_theta * np.sin(Theta)
Vy = V_theta * np.cos(Theta)

# Mask regions where there is no fluid (inside inner cylinder and outside outer cylinder)
Vx[(R < r_i) | (R > r_o)] = np.nan
Vy[(R < r_i) | (R > r_o)] = np.nan

# Create figure
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Add streamplot for velocity field
ax.streamplot(X, Y, Vx, Vy, density=1, linewidth=1, arrowsize=1)

# Render inner and outer cylinders
inner_cylinder = plt.Circle((0, 0), r_i, color='black', fill=True, label="Inner Cylinder")  # Filled black to indicate no fluid
inner_cylinder2 = plt.Circle((0,0), r_i-.1, color='white', fill=True, label="Inner Cylinder")
outer_cylinder = plt.Circle((0, 0), r_o, color='black', fill=False, linewidth=2, label="Outer Cylinder")


ax.add_patch(inner_cylinder)
ax.add_patch(outer_cylinder)
ax.add_patch(inner_cylinder2)

# Labels and title
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Velocity Field (Stable Taylor-Couette flow)")
plt.show()
