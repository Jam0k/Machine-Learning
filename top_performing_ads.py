import pandas as pd

# Read in the CSV file
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Calculate a score for each ad based on spend, clicks, and conversions
df['score'] = (df['spend'] * 0.5) + (df['clicks'] * 1.5) + (df['conversions'] * 2.0)

# Rank the ads by score
df_ranked = df.sort_values('score', ascending=False)

# Print out the top 10 performing ads with their scores
top_10 = df_ranked[['ad_name', 'spend', 'clicks', 'conversions', 'score']].head(10)

print("Top 10 performing ads:\n")
print(top_10)
