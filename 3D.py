import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def E(theta, phi):
    return -25 * np.sin(theta) * np.cos(phi)

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

Theta, Phi = np.meshgrid(theta, phi)
E_values = E(Theta, Phi)

E_max = np.max(E_values)
E_normalized = E_values / E_max

E_dB = 10 * np.log10(E_normalized)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(Theta, Phi, E_normalized, cmap='viridis')
ax.set_title('Normalized Radiation Power Pattern (3D)')
ax.set_xlabel('Theta (radians)')
ax.set_ylabel('Phi (radians)')
ax.set_zlabel('Normalized E')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(Theta, Phi, E_dB, cmap='viridis')
ax.set_title('Normalized Radiation Power Pattern (dB Scale) (3D)')
ax.set_xlabel('Theta (radians)')
ax.set_ylabel('Phi (radians)')
ax.set_zlabel('E (dB)')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()
