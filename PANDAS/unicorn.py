import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\Unicorn_Companies.csv')

print(df.head(15))
print()
print(df.info())
print()
print(df.describe())
print()
print(df.columns)
print()
print("Null values column wise")
print(df.isnull().sum())
print("Sum of total null values present")
print(df.isnull().sum().sum())
print()
print("Unique Contry Name")
print(df['Country'].nunique())
print(df['Country'].unique())
print()
print("Correlation Function")
x = df['Investors Count']
y = df['Portfolio Exits']
print(x.corr(y))

#c_matrix=df.corr(numeric_only=True)
#plt.figure(figsize(8,5))

#sns.heatmap(c_matrix,annot=True,cmap='coolwarm',fmt='2f',linewidth=0.85)
#plt.title("HeatMap of Unicorn DataSet")
#plt.show()

sns.histplot(df['Deal Term'],kde=True)
plt.show()

sns.boxplot(y=df['Deal Terms'])
plt.show()




        
