import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load your data set into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Convert the 'month' column to a datetime object
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

# Set the 'month' column as the index of the DataFrame
df.set_index('month', inplace=True)

# Group the data by month and calculate the average CPC for each month
cpc_by_month = df['cpc'].resample('M').mean()

# Fit an ARIMA model to the time series data
model = ARIMA(cpc_by_month, order=(1, 1, 1))
model_fit = model.fit()

# Specify the start and end dates for the prediction
start_date = cpc_by_month.index.max()
end_date = cpc_by_month.index.max() + pd.DateOffset(months=1)

# Make a prediction for the specified time range
forecast = model_fit.predict(start=start_date, end=end_date)

# Combine the time series data and the forecasted values into a single DataFrame
data = pd.concat([cpc_by_month, forecast], axis=0)

# Plot the time series data and the forecasted values
plt.figure(figsize=(10, 6))
plt.plot(data.index, data.values, label='Actual')
plt.plot(forecast.index, forecast.values, label='Forecast')
plt.legend(loc='upper left')
plt.title('CPC by Month with Forecast')
plt.xlabel('Month')
plt.ylabel('CPC')
plt.show()
