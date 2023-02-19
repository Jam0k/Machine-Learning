import pandas as pd
from sqlalchemy import create_engine

# Load your data set into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Calculate the clicks per campaign
clicks_per_campaign = df.groupby('campaign_name')['clicks'].sum()

# Predict the campaign with the highest clicks for the next month
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')
df.set_index('month', inplace=True)
clicks_by_month = df['clicks'].resample('M').sum()
start_date = clicks_by_month.index.max()
end_date = pd.to_datetime('2022-03')
forecast = clicks_by_month.diff().fillna(0).rolling(window=3).mean().iloc[-1]
best_campaign = clicks_per_campaign.idxmax()

# Calculate the engagement per campaign
engagement_per_campaign = df.groupby('campaign_name')['actions'].sum()

# Calculate the profit to engagement ratio
profit_to_engagement_ratio = df.groupby('campaign_name').apply(lambda x: x['profit'].sum() / x['actions'].sum())

# Connect to PostgreSQL instance
engine = create_engine('postgresql://root:root@localhost:5432/data')

# connection = engine.connect()

# Create ad_insights table
# connection.execute('CREATE TABLE IF NOT EXISTS ad_insights
#                   (id SERIAL PRIMARY KEY,
#                    campaign_name VARCHAR(255),
#                    clicks INTEGER,
#                    engagement INTEGER,
#                    profit_to_engagement_ratio FLOAT)')
with engine.connect() as connection:

    # Insert data into ad_insights table
    for campaign in clicks_per_campaign.index:
        clicks = clicks_per_campaign[campaign]
        engagement = engagement_per_campaign[campaign]
        ratio = profit_to_engagement_ratio[campaign]
        query = f"INSERT INTO ad_insights (campaign_name, clicks, engagement, profit_to_engagement_ratio) VALUES ('{campaign}', {clicks}, {engagement}, {ratio})"
        connection.execute(query)
        
    # Print the results
    print(f'Clicks per campaign:\n{clicks_per_campaign}\n')
    print(f'Next month\'s campaign with the highest clicks forecast: {best_campaign} (forecasted increase of {forecast:.2f} clicks)\n')
    print(f'Engagement per campaign:\n{engagement_per_campaign}\n')
    print(f'Profit to engagement ratio per campaign:\n{profit_to_engagement_ratio}')
