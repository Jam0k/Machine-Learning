import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Load your data set into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Convert the 'month' column to a datetime object
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

# Set the 'month' column as the index of the DataFrame
df.set_index('month', inplace=True)

# Group the data by month and calculate the total unique clicks for each month
unique_clicks_by_month = df['unique_clicks'].resample('M').sum()

# Fit an ARIMA model to the time series data
model = ARIMA(unique_clicks_by_month, order=(1, 1, 1))
model_fit = model.fit()

# Specify the start and end dates for the prediction
start_date = unique_clicks_by_month.index.max()
end_date = pd.to_datetime('2022-03')

# Make a prediction for the specified time range
forecast = model_fit.predict(start=start_date, end=end_date)

# Calculate the increase in unique clicks per month
current_month_unique_clicks = unique_clicks_by_month[-1]
next_month_unique_clicks = forecast[-1]
unique_clicks_increase = (next_month_unique_clicks - current_month_unique_clicks) / current_month_unique_clicks * 100

# Print the forecasted increase in unique clicks for the next month
print('Next month\'s unique clicks increase forecast: {:.2f}%'.format(unique_clicks_increase))
