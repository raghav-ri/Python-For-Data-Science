import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\StudentsPerformance.csv')
#print(df.head())
sns.histplot(df['math score'],kde=True)
plt.show()
Q1=df['math score'].quantile(0.25)
print("Q1",Q1)
Q3=df['math score'].quantile(0.75)
print("Q3",Q3)
IQR=Q3-Q1
print("IQR",IQR)
lower_bound=Q1-1.5*IQR
print("LB",lower_bound)
upper_bound=Q3+1.5*IQR
print("UB",upper_bound)
outlier=df[(df['math score']<lower_bound)|(df['math score']>upper_bound)]
print(outlier['math score'])

sns.scatterplot(x=df.index,y=df['math score'],color='blue',label='Normal')
sns.scatterplot(x=outlier.index,y=outlier['math score'],color='red',label='Outlier')
plt.show()


df_clean=df[(df['math score']>=lower_bound)&(df['math score']<=upper_bound)]
print(df_clean['math score'].head(20))

sns.heatmap(df.corr(numeric_only=True),annot=True,fmt='.2f',cmap='coolwarm')
# plt.show()

sns.boxplot(y=df_clean['math score'])
#plt.show()
