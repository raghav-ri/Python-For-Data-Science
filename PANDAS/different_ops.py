# import pandas as pd
# import numpy as np
# df1=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\demodata.csv')
# #print(df1)
# df1['Calories']=df1['Calories'].fillna(df1['Calories'].mean())
# print()
# #print(df1)
# df2=df1['Maxpulse'].max()
# print()
# #print(df2)
# df3=df1['Maxpulse'].min()
# #print(df3)
# df4=df1['Maxpulse'].std()
# print(df4)
# for i in df1.index:
#     if df1.loc[i,'Duration'] > 100:
#         df1.loc[i,'Duration']=90
# df1 = df1[df1['Pulse'] >= 10]





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
    if(df1.loc[i,'transmission']=="Manual"):   # manual_cars=df[df['transmission']=='Manual'] and  print(manual_cars.shape[0]) can print the number of rows present
        # print(df1.loc[i,'transmission']) # missing_data=df1.isnull().sum()
        count=count+1
print(count)
df1['engineSize']=df1['engineSize'].astype(int)