#drop dupilicate
#converting data_type
# handling outlier
#dropping column
#dropping record
#handling outlier
# handling missing value
# group by
#indexing
#df.drop_duplicates(inplace=True)
#df['Marks']=df['Marks'].astype(float)
#print(df.info())
#oulier
#df=df[df['Marks']>500]
#df.drop(columns=['Marks'],inplace=True)
#print(df)


import pandas as pd
import numpy as np
df1=pd.DataFrame({
    "Name":['Raghav','Raghav','Vishal',np.nan,np.nan,np.nan],
    "Marks":[500,500,300,96,54,np.nan]
    })

df2=pd.DataFrame({
    "Id":[101,102,103,104,105,106],
    "Mark":[394,495,583,387,909,343]
    })
result=df1.join(df2)
print(result)

