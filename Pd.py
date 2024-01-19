import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 1.0  # mass of the atom
spring_constant = 1.0  # force constant or spring constant
lattice_constant = 1.0  # separation between two atoms

# Define the range of k values
k_values = np.linspace(-np.pi / lattice_constant, np.pi / lattice_constant, 1000)

# Calculate angular frequency (omega) for each k
omega_values = np.sqrt(spring_constant / mass) * np.abs(np.sin(k_values * lattice_constant / 2))

# Plot the dispersion relation
plt.plot(k_values, omega_values)
plt.xlabel('k')
plt.ylabel('ω')
plt.title('Dispersion Relation for Monoatomic Lattice')
plt.grid(True)
plt.show()
