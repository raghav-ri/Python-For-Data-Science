from scipy.stats import uniform
a=0
b=30
x1=0
x2=10
#uniform distribution p(0<=x<=10)
prob=uniform.cdf(x2,loc=a,scale=b-a) - uniform.cdf(x1,loc=a,scale=b-a)
print(f"Probability bus arrives between 0 and 10 minutes: {prob:.2f}")

# cdf we are finding p()