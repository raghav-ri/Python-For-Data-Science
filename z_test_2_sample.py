# import pandas as pd
# import numpy as np
# from statsmodels.stats.weightstats import ztest
# df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\realistic_store_sales.csv')


# #z_test
# z_stat, p_value=ztest(df['Store_A'],df['Store_B'])

# print(f"Z_Statistic: {z_stat:.2f}")
# print(f"P_Value: {p_value:.4f}")

# alpha=0.05
# if(p_value<alpha):
#     print("Null Hypothesis is rejected")
# else:
#     print("Null Hypothesis is accepted")
 



import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\realistic_store_sales.csv')

print(df.columns)

z_stat,p_val=ztest(df['Store_A'],df['Store_B'])

print(f"Z_statistic {z_stat:.3f}")
print(f"p_value {p_val:.3f}")

alpha=0.05
if(alpha>p_val):
    print("Null Hypothesis is rejected")
else:
    print("Null Value is accepted")



# sample_1 = np.random.normal(loc=50, scale=5, size=100)  # Mean=50, StdDev=5, Size=100
# sample_2 = np.random.normal(loc=55, scale=5, size=100)  # Mean=55, StdDev=5, Size=100


# sample_1 = [12, 15, 14, 10, 13]
# sample_2 = [18, 20, 17, 19, 21]