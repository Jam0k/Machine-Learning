import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read the data into a pandas DataFrame
data = pd.read_csv("clickspend.csv")

# Select the relevant columns
data = data[["spend", "clicks"]]

# Split the data into training and testing sets
train_data = data[:int(len(data) * 0.8)]
test_data = data[int(len(data) * 0.2):]

# Train the linear regression model on the training data
X_train = train_data["spend"].values.reshape(-1, 1)
y_train = train_data["clicks"].values
reg = LinearRegression().fit(X_train, y_train)

# Use the trained model to make predictions on the test data
X_test = test_data["spend"].values.reshape(-1, 1)
y_test = test_data["clicks"].values
y_pred = reg.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Use the trained model to predict the number of clicks for a new ad
spend = float(input("Enter spend: "))
predicted_clicks = reg.predict([[spend]])
print("Predicted clicks:", predicted_clicks[0])