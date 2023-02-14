import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Sort the DataFrame by clicks in descending order and get the first row
best_ad_row = df.sort_values(by='clicks', ascending=False).iloc[0]

# Get the ad name, clicks, and other relevant data from the best performing ad row
ad_name = best_ad_row['ad_name']
clicks = best_ad_row['clicks']
conversions = best_ad_row['conversions']
spend = best_ad_row['spend']
currency_type = best_ad_row['account_currency']
cost_per_ad_click = best_ad_row['cost_per_ad_click']
cost_per_conversion = best_ad_row['cost_per_conversion']
age_targeting = best_ad_row['age_targeting']
gender_targeting = best_ad_row['gender_targeting']
ad_format_asset = best_ad_row['ad_format_asset']

# Print out statistics about the best performing ad
print(f"The best performing ad is '{ad_name}' with {clicks} clicks and {conversions} conversions.")
print(f"The ad received {spend}{currency_type} in spend, with a cost per ad click of {cost_per_ad_click}{currency_type} and a cost per conversion of {cost_per_conversion}{currency_type}.")
print(f"The ad targeted people between {age_targeting} years old and was primarily aimed at {gender_targeting}s.")
print(f"The ad format for this ad was {ad_format_asset}.")
