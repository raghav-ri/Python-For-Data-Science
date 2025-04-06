import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset('iris')
#  0   sepal_length  150 non-null    float64
#  1   sepal_width   150 non-null    float64
#  2   petal_length  150 non-null    float64
#  3   petal_width   150 non-null    float64
#  4   species       150 non-null    object

print(iris.info())
print(iris.head())
# sns.scatterplot(x='sepal_length',y='sepal_width',color='red',data=iris)
# sns.scatterplot(x='petal_length',y='petal_width',color='green',data=iris)
# #plt.show()

# sns.barplot(x='species',y='sepal_length',color='r',data=iris)
# sns.barplot(x='species',y='sepal_width',color='g',data=iris)
# #plt.show()

# sns.barplot(x='species',y='petal_length',color='r',data=iris)
# sns.barplot(x='species',y='petal_width',color='g',data=iris)
# #plt.show()

# sns.lineplot(x='sepal_length',y='petal_length',color='r',data=iris)
# sns.lineplot(x='sepal_width',y='petal_width',color='g',data=iris)
# plt.show()
print(iris['species'].value_counts())
print("Sepal Length Vs Sepal Width")
print(iris['sepal_length'].corr(iris['sepal_width']))
print("Petal length Vs Petal Width")
print(iris['petal_length'].corr(iris['petal_width']))
print("Petal length VS Sepal Width")
print(iris['petal_length'].corr(iris['sepal_width']))
print("Sepal length VS Petal Widtth")
print(iris['sepal_length'].corr(iris['petal_width']))
print("Petal length vs Sepal Length")
print(iris['petal_length'].corr(iris['sepal_length']))
print("Petal Width VS Sepal Width")
print(iris['petal_width'].corr(iris['sepal_width']))




