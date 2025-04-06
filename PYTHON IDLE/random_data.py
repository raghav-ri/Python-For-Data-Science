import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.DataFrame({
    'Category':np.random.choice(['A','B','C','D'],size=100),
    'Value1':np.random.randn(100),
    'Value2':np.random.randn(100)*10+50,
    'Date':pd.date_range(start='2023-08-11',periods=100,freq='D')
    })
df.to_csv('random.csv',index=False)
print(df)
sns.lineplot(x=df['Date'],y=df['Value1'])
plt.title("Time vs Value1")
plt.xticks(rotation=45)

sns.lineplot(x=df['Date'],y=df['Value2'],color='red')
plt.title("Time vs Value2")
plt.grid()
plt.xticks(rotation=45)
#plt.show()

sns.barplot(x=df['Category'],y=df['Value1'])
plt.title("Date vs Category")
plt.xticks(rotation=45)
plt.show()
pivot_df = df.pivot_table(index='Date', columns='Category', values='Value1', aggfunc='count', fill_value=0)
pivot_df.plot(kind='bar',stacked=True,colormap='viridis',figsize=(12,6))
plt.show()


sns.scatterplot(x='Value1',y='Value2',hue='Category',style='Category',s=100,data=df)
plt.title("Value1 vs Value2")
#plt.show()

palette={'A':'red','B':'blue','C':'green','D':'grey'}
markers={'A':'H','B':'P','C':'H','D':'*'}
sns.scatterplot(x='Value1',y='Value2',hue='Category',style='Category',palette=palette,markers=markers,s=100,data=df)
#plt.show()






         
