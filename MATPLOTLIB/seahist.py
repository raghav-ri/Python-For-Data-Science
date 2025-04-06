import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.DataFrame(
    {
        "A": [1, 2, 3, 4, 5,4,5,2,3,4,5,2,4,5,3,4,5,3,4,5,6]
       
    }
)
sns.histplot(df,bins=30,kde=True)
plt.show()