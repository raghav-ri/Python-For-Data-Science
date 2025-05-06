import scipy.stats as stats
data=[[30,10,10],[10,20,20]]
chi2,p,dof,expected=stats.chi2_contigency(data)  #degree of freedom
print(f"Chi2={chi2:.2f}")
print(f"P-value: {p:.4f}")
alpha=0.05
if p<alpha:
    print("Reject the null hypothesis: There is a significant association between major and preferrd program")
else:
    print("Fail to reject the null hypothesis: No significant association")