import numpy as np
import matplotlib.pyplot as plt
import geomstats.backend as gs
from geomstats.geometry.hyperbolic import Hyperbolic
from geomstats.geometry.euclidean import Euclidean

# Set random seed for reproducibility
np.random.seed(0)

# Define the Hyperbolic manifold
manifold = Hyperbolic(dimension=2)

# Define a non-expansive map (custom map for demonstration)
def non_expansive_map(point):
    return gs.array(point) + 0.1  # Example of a non-expansive map (adds a constant)

# Generate two random points on the manifold
p = manifold.random_uniform()
q = manifold.random_uniform()

# Apply the non-expansive map to the points
mapped_p = non_expansive_map(p)
mapped_q = non_expansive_map(q)

# Compute the distances before and after mapping
dist_pq = manifold.metric.dist(p, q)
dist_mapped_pq = manifold.metric.dist(mapped_p, mapped_q)

# Print the distances and check for Thomson's non-expansivity
print(f"Distance between p and q: {dist_pq:.4f}")
print(f"Distance between mapped_p and mapped_q: {dist_mapped_pq:.4f}")

if dist_mapped_pq <= dist_pq:
    print("Thomson's non-expansivity holds.")
else:
    print("Thomson's non-expansivity does not hold.")

# Visualization (optional)
fig = plt.figure(figsize=(10, 5))

# Plot the original points
ax1 = fig.add_subplot(121)
manifold.plot(p, ax=ax1, label='p', color='blue', marker='o')
manifold.plot(q, ax=ax1, label='q', color='red', marker='o')
ax1.set_title('Original Points')
ax1.legend()

# Plot the mapped points
ax2 = fig.add_subplot(122)
manifold.plot(mapped_p, ax=ax2, label='F(p)', color='blue', marker='o')
manifold.plot(mapped_q, ax=ax2, label='F(q)', color='red', marker='o')
ax2.set_title('Mapped Points')
ax2.legend()

plt.tight_layout()
plt.show()
