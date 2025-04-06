import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({
    'x':[1,2,3,4,5],
    'y':[1,4,9,16,25]
})
sns.lineplot(x='x',y='y',data=df)
plt.title("Seaborn Line Plot")
plt.show()