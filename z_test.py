# #one sample ztest
# import numpy as np
# from statsmodels.stats.weightstats import ztest

# data=[11.8]*100
# popu_mean=12
# popu_std_dev=0.5

# z_statistic, p_value=ztest(data,value=popu_mean)

# print(f"Z_Statistic: {z_statistic:.3f}")
# print(f"P_Value: {p_value:.3f}")

# alpha=0.05
# if(p_value<alpha):
#     print("Null Hypothesis is rejected")
# else:
#     print("Null Hypothesis is accepted")



from statsmodels.stats.weightstats import ztest
import numpy as np

# Generate sample data with variability
data = np.random.normal(loc=11.7, scale=1, size=100)  # Mean=11.7, StdDev=1, Size=100
popu_mean = 15

z_statistic, p_value = ztest(data, value=popu_mean)

print(f"Z Statistic value is {z_statistic:.3f} ")
print(f"P value is {p_value:.3f}")

alpha = 0.05
if alpha > p_value:
    print("Null Hypothesis is rejected")
else:
    print("Null Hypothesis is accepted")



