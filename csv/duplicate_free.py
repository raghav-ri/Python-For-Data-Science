import pandas as pd
import numpy as np
df=pd.read_csv('handl_miss.csv')
df_duplicate_free=df.drop_duplicates()
df_duplicate_free.to_csv('handl_miss_dup_free.csv',index=False)