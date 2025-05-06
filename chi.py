# import scipy.stats as stats
# data=[[30,10,10],[10,20,20]]
# chi2,p,dof,expected=stats.chi2_contingency(data)  #degree of freedom
# print(f"Chi2={chi2:.2f}")
# print(f"P-value: {p:.4f}")
# alpha=0.05
# if p<alpha:
#     print("Reject the null hypothesis: There is a significant association between major and preferrd program")
# else:
#     print("Fail to reject the null hypothesis: No significant association")


from scipy.stats import chi2_contingency

data=[[20,15,15],[19,11,9]]

chi_stat,p_value,d_o_f,expected_freq_null_hypo=chi2_contingency(data)

print(f"Chi Squared Statistic is: {chi_stat:.3f}")
print(f"P_value Statistic is: {p_value:.4f}")
print(f"Degree of freedom: {d_o_f:.4f}")
print(f"Expected frequency under null hypothesis: {expected_freq_null_hypo:.4f}")

alpha=0.05
if(alpha>p_value):
    print("NUll Hypothesis is rejected becaause there is significant association between major and preferred program")
else:
    print("Null Hypothesis is accepted because ther is not significant association between major and preferred progeamm")
