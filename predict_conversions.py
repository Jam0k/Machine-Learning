import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load the data into a Pandas DataFrame
data = pd.read_csv("fb_ad_insight_api_transpose.csv")

# Select the relevant columns for modeling
X = data[["ad_impression_actions", "ad_click_actions", "adset_id", "campaign_id", "clicks", "impressions", "conversion_values", "cost_per_action_type", "cost_per_conversion", "cost_per_unique_conversion"]].values
y = data["conversions"].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model and fit it to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the performance of the model using R-squared
r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)

# Define a new set of input data for prediction
new_data = np.array([[1000, 20, 900, 987654321, 3000, 50000, 1000, 5.0, 20.0, 30.0]])

# Make a prediction for the new data
prediction = model.predict(new_data)
print("Predicted conversions:", prediction)
