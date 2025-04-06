import pandas as pd

df1 = pd.read_csv('rv1.csv')
df2 = df1.dropna()
df2.to_csv('cleaned.csv',index=False)
print(df2.to_string())