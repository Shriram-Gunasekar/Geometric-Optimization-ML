from geomstats.geometry.hyperbolic import Hyperbolic

# Define the hyperbolic manifold
manifold = Hyperbolic(dimension=2)

# Check if a set is geodesically convex
points_set = np.array([[0.0, 0.0], [1.0, 0.5], [0.5, 1.5]])
is_geodesic_convex = manifold.is_geodesic_convex(points_set)

if is_geodesic_convex:
    print("The set is geodesically convex.")
else:
    print("The set is not geodesically convex.")
