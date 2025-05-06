import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

house_size=np.array([500,1000,1500,2000,2500]).reshape(-1,1)
house_price=np.array([100,150,200,250,300])

model=LinearRegression()
model.fit(house_size,house_price)

predict_price=model.predict(np.array([[1900]]))
print(f"Predict Price for a 1800 sq ft house:${predict_price[0]*1000:.2f}")


plt.scatter(house_size,house_price,color='blue',label='Actual data points')
plt.plot(house_size,model.predict(house_size),color='red',label='Regression line')
plt.xlabel("House Size(sq ft)")
plt.ylabel('Price($1000s)')
plt.title("ML Prediction")
plt.show()
