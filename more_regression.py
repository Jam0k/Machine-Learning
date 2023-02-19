import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
import numpy as np


# Load the data into a Pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Ad performance prediction
X_ad_perf = df[['actions', 'impressions', 'cpc', 'ctr']]
y_ad_perf = df['clicks']
model_ad_perf = LinearRegression()
model_ad_perf.fit(X_ad_perf, y_ad_perf)
new_data_ad_perf = pd.DataFrame([[300, 5000, 0.20, 0.05]], columns=X_ad_perf.columns)
prediction_ad_perf = model_ad_perf.predict(new_data_ad_perf)
print("Ad performance prediction: ", prediction_ad_perf)

# Audience behavior prediction
X_audience = df[['location']]

# One-hot encode the location column
encoder = OneHotEncoder()
X_audience_encoded = encoder.fit_transform(X_audience[['location']])
X_audience_encoded_df = pd.DataFrame.sparse.from_spmatrix(X_audience_encoded, columns=encoder.get_feature_names_out(['location']))
X_audience = pd.concat([X_audience_encoded_df], axis=1)

# Fit the KMeans model
model_audience = KMeans(n_clusters=4, n_init=10)
model_audience.fit(X_audience)

# Create new data for prediction
## new_data_audience = pd.DataFrame([[0, 0, 0, 1]], columns=X_audience.columns)
new_data_audience = pd.DataFrame([[0, 0, 0, 0, 0, 1, 0, 0]], columns=X_audience.columns)

prediction_audience = model_audience.predict(new_data_audience)
print("Audience behavior prediction: ", prediction_audience)

# Campaign outcomes prediction
df_campaign = df[['date_start', 'clicks']]
df_campaign.columns = ['ds', 'y']


# Calculate the total number of clicks over the last 30 days
df_campaign_last_30_days = df_campaign.tail(30)
predicted_clicks_campaign = df_campaign_last_30_days['y'].sum()

# Fit a linear regression model to the data
## X_campaign = pd.DataFrame(pd.to_datetime(df_campaign['ds'])).astype(int)

## X_campaign = (pd.to_datetime(df_campaign['ds']).values.astype('datetime64[D]') - np.datetime64('1970-01-01')).astype(int)

X_campaign = (pd.to_datetime(df_campaign['ds']).values.astype('datetime64[D]') - np.datetime64('1970-01-01')).astype(int).reshape(-1, 1)


y_campaign = df_campaign['y']
model_campaign = LinearRegression()
model_campaign.fit(X_campaign, y_campaign)




# Predict the number of clicks for the next 30 days
## next_30_days = pd.date_range(start=df_campaign['ds'].iloc[-1], periods=30, freq='D')
## X_campaign_pred = pd.DataFrame(next_30_days).astype(int)
## predicted_clicks_campaign += int(model_campaign.predict(X_campaign_pred).sum())

# create input data
next_30_days = pd.date_range(start=df_campaign['ds'].iloc[-1], periods=30, freq='D')
## X_campaign_pred = pd.DataFrame(next_30_days).astype(int)

X_campaign_pred = (next_30_days - pd.Timestamp('1970-01-01')) // pd.Timedelta('1s')
X_campaign_pred = pd.DataFrame(X_campaign_pred).astype(int)


# reshape input data
X_campaign_pred_2d = X_campaign_pred.values.reshape(-1, 1)

# predict the number of clicks for the next 30 days
predicted_clicks_campaign += int(model_campaign.predict(X_campaign_pred_2d).sum())


print("clicks outcomes prediction 30 days: ", predicted_clicks_campaign)
