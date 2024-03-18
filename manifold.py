import numpy as np
import matplotlib.pyplot as plt
import geomstats.backend as gs
from geomstats.geometry.hyperbolic import Hyperbolic

# Define the hyperbolic manifold
manifold = Hyperbolic(dimension=2)

# Generate random points on the manifold
n_samples = 100
points = manifold.random_uniform(n_samples=n_samples)

# Plot the points on the manifold
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1])
plt.title('Random Points on Hyperbolic Manifold')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
