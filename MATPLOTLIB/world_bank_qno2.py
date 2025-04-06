import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df1=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\WorldBank.csv')

df1=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\WorldBank.csv')
print(df1.head())
print(df1.columns)
print(df1.info())


# qno1(Matplotlib)
country='India'
df2=df1[df1['Country Name']==country]
year =df2['Year']
gdp=df2['GDP (USD)']
plt.plot(year,gdp)
plt.title("GDP of Countries")
plt.xlabel("Year")
plt.ylabel("GDP (USD)")
plt.xticks(rotation=90)
plt.show()

# Seaborn
sns.lineplot(x='Year',y='GDP (USD)',data=df2)
plt.title("GDP of Countries")
plt.xlabel("Year")
plt.ylabel("GDP (USD)")
plt.xticks(rotation=90)
plt.show()



#qno2 Matplotlib
year=2018
df3=df1[df1['Year']==year].nlargest(10,'GDP (USD)')
plt.bar(df3['Country Name'],df3['GDP (USD)'])
plt.title(f"GDP of Countries in {year}")
plt.xlabel("Country Name")
plt.ylabel("GDP (USD)")
plt.show()

#seaborn
sns.barplot(x='Country Name',y='GDP (USD)',data=df3,palette='viridis')
plt.title("GDP of Countries")
plt.xlabel("Country Name ")
plt.ylabel("GDP (USD) seaborn")
plt.xticks(rotation=90)
plt.show()

#qno3
gdpp=df1['GDP (USD)'].dropna()
plt.hist(gdpp,bins=5,edgecolor='green')
plt.xlabel('GDP (USD)')
plt.ylabel('Frequency')
plt.title('GDP Distribution')
plt.show()


#seaborn
sns.histplot(x=gdpp,bins=5,edgecolor='grey',kde=True)
plt.xlabel('GDP (USD)')
plt.ylabel('Frequency seaborn')
plt.title("GDp Distribution")
plt.show()



#qno4
plt.scatter(df1['Population density (people per sq. km of land area)'],df1['GDP (USD)'])
plt.title('Population Density vs GDP')
plt.xlabel('Population Density (people per sq. km of land area)')
plt.ylabel('GDP (USD)')
# plt.xscale('log')
# plt.yscale('log')
plt.grid(True)
plt.show()

#seaborn
sns.scatterplot(x="Population density (people per sq. km of land area)",y="GDP (USD)",data=df1)
plt.show()
