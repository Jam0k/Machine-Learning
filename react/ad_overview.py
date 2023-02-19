import pandas as pd
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="root",
    password="root"
)

# Query the database and load the results into a pandas DataFrame
df = pd.read_sql("SELECT * FROM fb_ad_insight_api_transpose", conn)

# Calculate and print the most frequently occurring "ad_format_asset"
most_common_ad_format_asset = df['ad_format_asset'].mode()[0]
print(f"The most frequently occurring ad_format_asset is {most_common_ad_format_asset}")

# Calculate and print the average "auction_bid"
avg_auction_bid = df['auction_bid'].mean()
print(f"The average auction_bid is {avg_auction_bid}")

# Calculate and print the most frequently occurring "auction_competitiveness"
most_common_auction_competitiveness = df['auction_competitiveness'].mode()[0]
print(f"The most frequently occurring auction_competitiveness is {most_common_auction_competitiveness}")

# Calculate and print the average "clicks"
avg_clicks = df['clicks'].mean()
print(f"The average clicks is {avg_clicks}")

# Calculate and print the average "conversions"
avg_conversions = df['conversions'].mean()
print(f"The average conversions is {avg_conversions}")

# Calculate and print the average "cost_per_unique_click"
avg_cost_per_unique_click = df['cost_per_unique_click'].mean()
print(f"The average cost_per_unique_click is {avg_cost_per_unique_click}")

# Calculate and print the average "cost_per_unique_conversion"
avg_cost_per_unique_conversion = df['cost_per_unique_conversion'].mean()
print(f"The average cost_per_unique_conversion is {avg_cost_per_unique_conversion}")

# Calculate and print the most frequently occurring "country"
most_common_country = df['country'].mode()[0]
print(f"The most frequently occurring country is {most_common_country}")

# Calculate and print the average "cpc"
avg_cpc = df['cpc'].mean()
print(f"The average cpc is {avg_cpc}")

# Calculate and print the average "cpm"
avg_cpm = df['cpm'].mean()
print(f"The average cpm is {avg_cpm}")

# Calculate and print the average "cpp"
avg_cpp = df['cpp'].mean()
print(f"The average cpp is {avg_cpp}")

# Calculate and print the best performing ad based on clicks and conversions
best_ad = df.iloc[df[['clicks', 'conversions']].sum(axis=1).idxmax()]

# Print the associated costs and statistics
print(f"The best performing ad is {best_ad['ad_name']}")
print(f"It received {best_ad['clicks']} clicks, {best_ad['conversions']} conversions, and had a cost_per_unique_click of {best_ad['cost_per_unique_click']} and a cost_per_unique_conversion of {best_ad['cost_per_unique_conversion']}.")
