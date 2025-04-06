import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\combined (1).csv')
print(df.columns)
#qno1
print(df['Cust_id'].unique())
print(df['Cust_id'].nunique())

#qno2
print(df['Sales'].sum())

#qno3
#which product category has highest sales
ad=df.groupby('Product_Category')['Profit'].sum()
# print(ad)
# print(ad.max())
print(ad.idxmax())


#qno4
#avg discount applied on orders
print(df['Discount'].mean())


#qno5
#which shopping mode is used frquently
ad1=df['Ship_Mode'].value_counts()
print(ad1.idxmax())
# print(ad1.max())



#qno6
#corelation between sales and profit
print(df['Sales'].corr(df['Profit']))


