from scipy.stats import uniform
a=0
b=30
x1=0
x2=10
#uniform distribution p(0<=x<=10)
prob=uniform.cdf(x2,loc=a,scale=b-a) - uniform.cdf(x1,loc=a,scale=b-a)
print(f"Probability bus arrives between 0 and 10 minutes: {prob:.2f}")

# cdf we are finding p()
# The question being addressed in the code is likely:

# **"What is the probability that a bus arrives between 0 and 10 minutes if the arrival time follows a uniform distribution between 0 and 30 minutes?"**

# This is a typical question involving the **Uniform Distribution** and the calculation of probabilities using the **Cumulative Distribution Function (CDF)**.



# Identify the Range (a and b):

# a: The minimum value of the range (e.g., 0 minutes in the question).
# b: The maximum value of the range (e.g., 30 minutes in the question).
# Subrange (x1 and x2):GitHub Copilot
# How to Identify That the Question is About Uniform Distribution:
# Key Characteristics of Uniform Distribution:

# The probability is evenly distributed across a range of values.
# Every value within the range is equally likely to occur.
# The question explicitly mentions a range (e.g., "between 0 and 30 minutes").
# Clues in the Question:

# The question specifies a range of values (e.g., "arrival time between 0 and 30 minutes").
# The question asks for the probability of an event occurring within a subrange of the total range (e.g., "between 0 and 10 minutes").
# There is no mention of a peak or skewness in the distribution, which rules out other distributions like normal or exponential.
# Uniform Distribution Formula:

# The probability density function (PDF) for a uniform distribution is:

# where a is the lower bound and b is the upper bound of the range.

# The cumulative distribution function (CDF) is:

# How to Choose Parameters for Uniform Distribution:
# Identify the Range (a and b):

# a: The minimum value of the range (e.g., 0 minutes in the question).
# b: The maximum value of the range (e.g., 30 minutes in the question).
# Subrange (x1 and x2):

# x1: The lower bound of the subrange for which you want to calculate the probability (e.g., 0 minutes).
# x2: The upper boun