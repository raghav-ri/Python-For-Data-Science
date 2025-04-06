import pandas as pd
df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\irregular_dataset.csv')
print(df.head())
print()
print(df.tail())
print(df.shape)
print(df.info())
df.dropna(subset=['ID'],inplace=True)
df.dropna(inplace=True)
df.to_csv(r"C:\Users\RAMAN\Desktop\Python CSV\irregular_dataset.csv", index=False)
print(df.info())
df['Age']=df.fillna(df['Age'].mean())


# print(df.describe())