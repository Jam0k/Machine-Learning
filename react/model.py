from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="root",
    password="root"
)

# Load the data from the database
data = pd.read_sql("SELECT campaign_name, clicks, impressions, actions, spend, profit FROM fb_ad_insight_api_transpose", conn)

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
results = []
for campaign in campaigns:
    X_train = X[campaign]
    y_train = y[campaign]
    predictions = {}
    if len(y_train.unique()) > 1: # Only fit logistic regression if there are multiple classes
        for model_name, model in models.items():
            if model_name == 'Polynomial Regression':
                poly = model
                X_train_poly = poly.fit_transform(X_train)
                model = LinearRegression()
                model.fit(X_train_poly, y_train)
                new_data_poly = poly.fit_transform(new_data)
                predictions[model_name] = model.predict(new_data_poly)
            else:
                model.fit(X_train, y_train)
                predictions[model_name] = model.predict(new_data)
    else:
        # If there's only one class, assign the same prediction to all input data
        for model_name in models:
            predictions[model_name] = [y_train.iloc[0]] * len(new_data)
    result = {
        'campaign_name': campaign,
        'linear_regression': predictions['Linear Regression'][0],
        'polynomial_regression': predictions['Polynomial Regression'][0],
        'random_forest_regression': predictions['Random Forest Regression'][0],
        'logistic_regression': predictions['Logistic Regression'][0]
    }
    results.append(result)
    # Insert the results into the 'results' table in the database
    cur = conn.cursor()
    cur.execute("INSERT INTO results (campaign_name, linear_regression, polynomial_regression, random_forest_regression, logistic_regression) VALUES (%s, %s, %s, %s, %s)", (result['campaign_name'], result['linear_regression'], result['polynomial_regression'], result['random_forest_regression'], result['logistic_regression']))
    conn.commit()
    cur.close
