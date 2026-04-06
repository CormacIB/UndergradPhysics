import numpy as np
import matplotlib.pyplot as plt

k_vals = np.linspace(0.1, 10, 500)
Ta_vals = np.linspace(0, 5000, 400)

def growth_rate(k, Ta):
    Ta_neutral = (k**2 + np.pi**2)**3 / k**2
    return Ta - Ta_neutral  # positive = unstable, negative = stable

growth_rates = np.array([[growth_rate(k, Ta) for k in k_vals] for Ta in Ta_vals])

plt.figure(figsize=(8, 6))
plt.contour(k_vals, Ta_vals, growth_rates, levels=[0], colors='red', linewidths=2)
plt.contourf(k_vals, Ta_vals, growth_rates, levels=np.linspace(-3000, 3000, 50), cmap='coolwarm_r', alpha=0.75)
plt.xlabel('Wavenumber $k$')
plt.ylabel('Taylor Number $Ta$')
plt.title('Marginal Stability Diagram — Taylor-Couette')
plt.colorbar(label='Growth Rate $\\omega_i$')
plt.grid()
plt.show()