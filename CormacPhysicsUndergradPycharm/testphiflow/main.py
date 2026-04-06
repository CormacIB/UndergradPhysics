import pylab
import matplotlib.pyplot as plt
from phi.torch.flow import *
from matplotlib.animation import FuncAnimation


smoke = CenteredGrid(0, extrapolation.BOUNDARY, x=32, y=40, bounds=Box(x=40, y=40))  # sampled at cell centers
velocity = StaggeredGrid(0, extrapolation.ZERO, x=32, y=40, bounds=Box(x=40, y=40))  # sampled in staggered form at face centers

INFLOW_LOCATION = tensor([(4, 5), (8, 5), (12, 5), (16, 5)], batch('inflow_loc'), channel(vector='x,y'))
INFLOW = .6 * CenteredGrid(Sphere(center=INFLOW_LOCATION, radius=8), extrapolation.BOUNDARY, x=32, y=40, bounds=Box(x=32, y=40))

print(f"Smoke: {smoke.shape}")
print(f"Velocity: {velocity.shape}")
print(f"Inflow: {INFLOW.shape}")
print(f"Inflow, spatial only: {INFLOW.shape.spatial}")

print(smoke.values)
print(velocity.values)
print(INFLOW.values)

trajectory = [smoke]
for i in range(20):
  print(i, end=' ')
  smoke = advect.mac_cormack(smoke, velocity, dt=1) + INFLOW
  buoyancy_force = smoke * (0, 0.5) @ velocity
  velocity = advect.semi_lagrangian(velocity, velocity, dt=1) + buoyancy_force
  velocity, _ = fluid.make_incompressible(velocity)
  trajectory.append(smoke)
trajectory = field.stack(trajectory, batch('time'))

vis.plot(smoke, animate='time')
vis.show()
