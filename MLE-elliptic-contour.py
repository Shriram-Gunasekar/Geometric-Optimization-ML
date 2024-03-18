import numpy as np
from scipy.optimize import minimize

# Set random seed for reproducibility
np.random.seed(0)

# Generate synthetic data from a multivariate normal distribution
mean_true = np.array([1, 2])  # True mean
cov_true = np.array([[2, 0.5], [0.5, 1]])  # True covariance matrix
sample_size = 1000  # Number of samples
data = np.random.multivariate_normal(mean_true, cov_true, size=sample_size)

# Define the negative log-likelihood function for the multivariate normal distribution
def neg_log_likelihood(params, data):
    mean = params[:2]
    cov = np.array([[params[2], params[3]], [params[3], params[4]]])
    n = data.shape[0]
    constant_term = -0.5 * n * np.log(2 * np.pi) - 0.5 * n * np.log(np.linalg.det(cov))
    quadratic_term = -0.5 * np.sum((data - mean) @ np.linalg.inv(cov) * (data - mean), axis=1)
    return -(constant_term + quadratic_term.sum())

# Initial guess for the parameters
initial_guess = np.array([0, 0, 1, 1, 1])

# Optimize the negative log-likelihood function using SciPy's minimize function
result = minimize(neg_log_likelihood, initial_guess, args=(data,), method='Nelder-Mead')

# Extract the MLE parameters from the optimization result
mle_mean = result.x[:2]
mle_cov = np.array([[result.x[2], result.x[3]], [result.x[3], result.x[4]]])

# Print the MLE parameters and true parameters for comparison
print("Maximum Likelihood Estimates:")
print("Mean:", mle_mean)
print("Covariance Matrix:")
print(mle_cov)

print("\nTrue Parameters:")
print("Mean:", mean_true)
print("Covariance Matrix:")
print(cov_true)
