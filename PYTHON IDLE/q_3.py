import pandas as pd

df1 = pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\Cardiotocographic.csv')


df1.dropna(inplace=True)


df1 = df1[df1['LB'] < 150]

variance_mode = df1['Variance'].mode()[0]
df1 = df1[df1['Variance'] == variance_mode]

print(df1)
