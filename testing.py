import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Fixed typo in 'pylplot'
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error  # Corrected function name

# Load dataset
diamonds = sns.load_dataset('diamonds')  # Corrected dataset name
X = diamonds[['carat']].values
y = diamonds['price'].values

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)  # Corrected function name
print(f"Mean Squared Error on Test Set: {mse:.2f}")

# Predict price for user-input carat value
input_carat = float(input("Enter the carat value of the diamond: "))
predicted_price = model.predict(np.array([[input_carat]]))  # Fixed typo in 'predict'
print(f"Predicted Price of the diamond: ${predicted_price[0]:.2f}")

# Plot actual vs. predicted values
plt.scatter(X_test, y_test, color='blue', label='Actual prices', alpha=0.5)  # Fixed incorrect variable name
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Carat')
plt.ylabel('Price (USD)')
plt.title("Diamond Price Prediction based on Carat")
plt.legend()
plt.show()
