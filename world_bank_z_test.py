import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\WorldBank.csv')
print(df.columns)

india_gdp=df[df['Country Name']=='India']['GDP (USD)']
