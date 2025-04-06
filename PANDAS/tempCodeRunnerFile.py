import pandas as pd
import numpy as np
df1=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\skoda.csv')
print(df1.head(15))
print()
print(df1.iloc[100:250])
print()
print(df1['price'].describe().round(2))

count=0
for i in df1.index:
    if(df1.loc[i,'transmission']=="Manual"):
        print(df1.loc[i,'transmission'])
        count=count+1
print(count)
df1['engineSize']=df1['engineSize'].astype('Int16')