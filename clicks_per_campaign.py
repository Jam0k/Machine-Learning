import pandas as pd

# Load your data set into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Group the data by campaign name and calculate the total clicks for each campaign
clicks_by_campaign = df.groupby('campaign_name')['clicks'].sum()

# Print the clicks by campaign
print(clicks_by_campaign)
