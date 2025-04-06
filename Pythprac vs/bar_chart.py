import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.DataFrame({
    "Fruit":["Apple","Mango","Litchi","Guava","Orange"],
    "Sales":[100,150,320,561,200],
    "Quantity":[10,15,32,56,20]
})
categories=data['Fruit']
values=data['Sales']
values1=data['Quantity']
x=np.arange(len(categories))
bar_width=0.35
plt.bar(x-bar_width/2,values,width=bar_width,color='g',label='Sales')
plt.bar(x+bar_width/2,values1,width=bar_width,color='r',label='Quantity')
plt.xlabel("Fruits")
plt.ylabel("Sales and Quantity")
plt.title("Fruit Sales")
plt.xticks(x,categories)
plt.show()