import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp,ttest_ind

df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\realistic_store_sales.csv')

population_mean=50
t_stat_1samp,p_val_1samp=ttest_1samp(df['Store_A'],population_mean)

print("1 Sample T_test")
print(f"T Statistic: {t_stat_1samp:.4f}")
print(f"P_value: {p_val_1samp:.4f}")


t_stat_2samp,p_val_2samp=ttest_ind(df['Store_A'],df['Store_B'])

print("2 Sample test")
print(f"T statistic :{t_stat_2samp:.4f}")
print(f"P_value: {p_val_2samp:.4f}")

alpha=0.05


if(alpha>p_val_1samp):
    print("Null Hypothesis is Rejected")
else:
    print("Null Hypothesis is Accepted")


if(alpha>p_val_2samp):
    print("Null Hypothesis is Rejected")
else:
    print("Null Hypothesis is Accepted")