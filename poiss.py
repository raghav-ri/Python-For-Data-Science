from scipy.stats import poisson
#lam =average rate
lam=3
k=5
#(mu )=average rate (mean)
#k=actual number of events
# e=Euler's number=2.718
#PMF probability of getting exactly 5 calls
prob=poisson.pmf(k,mu=lam)
print(f"P(X={k})={prob:.4f}")
# so ther is 10.08% chance that exactly 5 callls will arrive in an hour
