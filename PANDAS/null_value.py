# import numpy as np
# import pandas as pd

# df1 = pd.DataFrame({
#     'Eid': [1, np.nan, 3,5,6,7,8,9],
#     'Salary': [5000, 20000, np.nan,8000,9600,2511,3612,np.nan]

# })
# # df1.fillna(234,inplace=True)
# print(df1)
# df1.to_csv(r'C:\Users\RAMAN\Desktop\PYTHON TOOL BOX\csv\rv1.csv',index=False)




# import pandas as pd`6790-`
# df1=pd.read_csv('rv.csv')
# print(df1.to_string()) # why data cleaning is required 1 empty cells 2.data in wrong format 3. wrong data 4. duplicates
# by default dropna() method return a new Data Frame,and will not change the original but dropna(inplace=True) will not return a new Data Frame

import pandas as pd
import numpy as np
df1=pd.DataFrame({
    "Name":['Raghav','Raghav','Vishal',np.nan,np.nan,np.nan],
    "Marks":[500,500,300,96,54,np.nan]
    })

df2=pd.DataFrame({
    "Id":[101,102,103,104,105,106],
    "Marks":[394,495,583,96,300,500]
    })
result=pd.merge(df1,df2,on='Marks')
print(result)