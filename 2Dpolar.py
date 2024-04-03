import numpy as np
import matplotlib.pyplot as plt

def E(theta, phi):
    return -25 * np.sin(theta) * np.cos(phi)

theta = np.linspace(0, np.pi, 500)
phi = np.linspace(0, 2 * np.pi, 500)

Theta, Phi = np.meshgrid(theta, phi)
E_values = E(Theta, Phi)

E_max = np.max(E_values)
E_normalized = E_values / E_max

E_dB = 10 * np.log10(E_normalized)

fig_linear = plt.figure(figsize=(10, 5))
ax_linear = fig_linear.add_subplot(121, polar=True)
c_linear = ax_linear.contourf(Phi, Theta, E_normalized, cmap='viridis')
ax_linear.set_title('Normalized Radiation Power Pattern (Linear Scale)')
fig_linear.colorbar(c_linear, ax=ax_linear, label='Normalized E')

ax_dB = fig_linear.add_subplot(122, polar=True)
c_dB = ax_dB.contourf(Phi, Theta, E_dB, cmap='viridis')
ax_dB.set_title('Normalized Radiation Power Pattern (dB Scale)')
fig_linear.colorbar(c_dB, ax=ax_dB, label='E (dB)')

plt.tight_layout()
plt.show()