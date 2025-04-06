import pandas as pd
import numpy as np
df=pd.DataFrame({
    'Name':['Raghav','Ravi','Satyam','Arpit','Shubham','Rohan',np.nan,'Keshav','Tripurari','Murari','Shyam',np.nan],
    'Age':[21,np.nan,22,25,26,np.nan,41,12,np.nan,32,np.nan,21]
})
df['Age']=df['Age'].fillna(df['Age'].median())
df['Name']=df['Name'].fillna("Unkonwn")
df.to_csv('handl_miss.csv',index=False)
#removing duplicates , converting datatype, handling outlier,reset index,info(),describe()
