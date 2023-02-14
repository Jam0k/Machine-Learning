import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Get the ad_name input from the user
ad_name = input("Enter the name of the ad: ")

# Filter the DataFrame to get the row with the specified ad_name
ad_stats = df.loc[df['ad_name'] == ad_name]

# Check if the ad_name was found in the DataFrame
if ad_stats.empty:
    print(f"No statistics found for ad: {ad_name}")
else:
    # Get the relevant statistics from the ad_stats DataFrame
    ad_format_asset = ad_stats['ad_format_asset'].values[0]
    currency_type = ad_stats['account_currency'].values[0]
    age_targeting = ad_stats['age_targeting'].values[0]
    clicks = ad_stats['clicks'].values[0]
    conversions = ad_stats['conversions'].values[0]
    cost_per_ad_click = ad_stats['cost_per_ad_click'].values[0]
    cost_per_conversion = ad_stats['cost_per_conversion'].values[0]
    dma = ad_stats['dma'].values[0]
    gender_targeting = ad_stats['gender_targeting'].values[0]
    impressions = ad_stats['impressions'].values[0]
    objective = ad_stats['objective'].values[0]
    optimization_goal = ad_stats['optimization_goal'].values[0]
    spend = ad_stats['spend'].values[0]

    # Print the statistics
    print(f"Statistics for ad: {ad_name}")
    print(f"Ad format: {ad_format_asset}")
    print(f"Spend: {currency_type}{spend}")
    print(f"Target demographic: {age_targeting} years old, {gender_targeting}")
    print(f"Clicks: {clicks}")
    print(f"Conversions: {conversions}")
    print(f"Cost per ad click: {currency_type}{cost_per_ad_click}")
    print(f"Cost per conversion: {currency_type}{cost_per_conversion}")
    print(f"Designated market area (DMA): {dma}")
    print(f"Impressions: {impressions}")
    print(f"Objective: {objective}")
    print(f"Optimization goal: {optimization_goal}")
