import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean = 50  # Mean (μ)
std_dev = 10  # Standard Deviation (σ)

# Generate data
data = np.random.normal(loc=mean, scale=std_dev, size=1000)

# Plot the histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='blue', label='Histogram')

# Plot the PDF (Probability Density Function)
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
pdf = norm.pdf(x, loc=mean, scale=std_dev)
plt.plot(x, pdf, 'r', label='PDF (Normal Curve)')

# Add labels and legend
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()