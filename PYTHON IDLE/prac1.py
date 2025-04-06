import numpy as np
import pandas as pd
df=pd.DataFrame({
    "Name":['Raghav','Kumar','Issar'],
    "Age":[12,15,np.nan]
    })
df.fillna(18,inplace=True)
print(df)
