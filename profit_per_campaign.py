import pandas as pd

# Load your data set into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Calculate the profit to engagement ratio for each campaign
df['profit_engagement_ratio'] = df['profit'] / df['actions']

# Group the data by campaign name and calculate the mean profit to engagement ratio for each campaign
mean_profit_engagement_ratio_by_campaign = df.groupby('campaign_name')['profit_engagement_ratio'].mean()

# Print the results
print(mean_profit_engagement_ratio_by_campaign)
