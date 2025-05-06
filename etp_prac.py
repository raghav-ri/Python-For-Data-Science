import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

Experience = np.array([15, 12, 8, 11, 7, 3]).reshape(-1, 1)
Salary = np.array([40000, 35000, 28000, 30500, 20000, 12000])

model = LinearRegression()
model.fit(Experience, Salary)


predict_price = model.predict(np.array([[30]]))
print("Predicted price is: ", predict_price)


plt.scatter(Experience, Salary, color='blue', label='Data Points')
plt.plot(Experience, model.predict(Experience), color='red', label='Regression Line')
plt.legend()
plt.show()