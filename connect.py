import pandas as pd
import psycopg2
import json

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

# Convert the results to JSON format
clicks_per_campaign_json = json.dumps(clicks_per_campaign.to_dict())
engagement_per_campaign_json = json.dumps(engagement_per_campaign.to_dict())
profit_to_engagement_ratio_json = json.dumps(profit_to_engagement_ratio.to_dict())

# Define the connection parameters for the PostgreSQL instance
host = 'localhost'
port = 5432
dbname = 'data'
user = 'root'
password = 'root'

try:
    # Connect to the PostgreSQL instance
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS data.ad_insights
                  (id SERIAL PRIMARY KEY,
                   clicks_per_campaign JSONB,
                   best_campaign VARCHAR(255),
                   forecast FLOAT,
                   engagement_per_campaign JSONB,
                   profit_to_engagement_ratio JSONB)''')

    # Insert the data into the table
    cur.execute("INSERT INTO data.ad_insights (clicks_per_campaign, best_campaign, forecast, engagement_per_campaign, profit_to_engagement_ratio) VALUES (%s, %s, %s, %s, %s)",
                (clicks_per_campaign_json, best_campaign, forecast, engagement_per_campaign_json, profit_to_engagement_ratio_json))

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

except (Exception, psycopg2.DatabaseError) as error:
    print('Error while inserting data into PostgreSQL database:', error)
