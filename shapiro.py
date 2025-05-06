from scipy.stats import shapiro

data=[12,15,10,9,18,11,16,14,13]
stat, p_value=shapiro(data)
print(f"Shapiro-Wilk-Test Statistics:{stat:.3f}")
print(f"P-value: {p_value:.5f}")
if p_value<0.05:
    print("Data is normally Distributed {reject H0}")
else:
    print("Data is normally distributed{failed to reject H0}")


    
# Null Hypothesis (H₀): The data is normally distributed.
# Alternative Hypothesis (H₁): The data is not normally distributed.