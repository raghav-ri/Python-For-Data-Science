from scipy.stats import binom
# parameter
n=10
p=0.5
k=6
# pmf probability of exactly 6 success
prob=binom.pmf(k,n,p)
print(f"P(X= {k})={prob:.4f}")
#there is about a 20.15% chance you will get exactly 6 heads when you toss af fair coin 10 times
#pmf probability mass function'
# TOSS a coin to get 6 success