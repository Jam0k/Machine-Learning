from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# Load the data
data = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Get the unique campaign names
campaigns = data['campaign_name'].unique()

# Define the input and output variables for each campaign
X = {}
y = {}
for campaign in campaigns:
    X[campaign] = data[data['campaign_name'] == campaign][['clicks', 'impressions', 'actions', 'spend']]
    y[campaign] = data[data['campaign_name'] == campaign]['profit']

# Define the regression models for each campaign
models = {
    'Linear Regression': LinearRegression(),
    'Polynomial Regression': PolynomialFeatures(degree=2),
    'Random Forest Regression': RandomForestRegressor(n_estimators=100),
    'Logistic Regression': LogisticRegression(max_iter=10000)
}

# Fit the models and make predictions for new data points
new_data = pd.DataFrame({'clicks': [500, 1000, 2000], 'impressions': [1000, 2000, 4000], 'actions': [50, 100, 200], 'spend': [100, 200, 400]})
predictions = {}
for campaign in campaigns:
    X_train = X[campaign]
    y_train = y[campaign]
    predictions[campaign] = {}
    if len(y_train.unique()) > 1: # Only fit logistic regression if there are multiple classes
        for model_name, model in models.items():
            if model_name == 'Polynomial Regression':
                poly = model
                X_train_poly = poly.fit_transform(X_train)
                model = LinearRegression()
                model.fit(X_train_poly, y_train)
                new_data_poly = poly.fit_transform(new_data)
                predictions[campaign][model_name] = model.predict(new_data_poly)
            else:
                model.fit(X_train, y_train)
                predictions[campaign][model_name] = model.predict(new_data)
    else:
        # If there's only one class, assign the same prediction to all input data
        for model_name in models:
            predictions[campaign][model_name] = [y_train.iloc[0]] * len(new_data)

# Print the predictions for each campaign and regression type
for campaign in campaigns:
    print(f'Campaign {campaign}')
    for model_name, prediction in predictions[campaign].items():
        print(f'{model_name}: {prediction}')
