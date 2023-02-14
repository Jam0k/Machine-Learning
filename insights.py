import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Get the row with the highest spend.
highest_spend_row = df.loc[df['spend'].idxmax(), ['ad_name', 'spend', 'ad_format_asset', 'account_currency', 'age_targeting', 'clicks', 'conversions', 'cost_per_ad_click', 'cost_per_conversion', 'dma', 'gender_targeting', 'impressions', 'objective', 'optimization_goal']]

# Get the ad_name and spend value from the highest spend row.
ad_name = highest_spend_row['ad_name']
spend = highest_spend_row['spend']

# Get the ad_format_asset from the highest spend row.
ad_format_asset = highest_spend_row['ad_format_asset']

# Get the currency type from the highest spend row.
currency_type = highest_spend_row['account_currency']

# Get the age_targeting from the highest spend row.
age_targeting = highest_spend_row['age_targeting']

# Get the clicks from the highest spend row.
clicks = highest_spend_row['clicks']

# Get the conversions from the highest spend row.
conversions = highest_spend_row['conversions']

# Get the cost_per_ad_click from the highest spend row.
cost_per_ad_click = highest_spend_row['cost_per_ad_click']

# Get the cost_per_conversion from the highest spend row.
cost_per_conversion = highest_spend_row['cost_per_conversion']

# Get the dma from the highest spend row.
dma = highest_spend_row['dma']

# Get the gender_targeting from the highest spend row.
gender_targeting = highest_spend_row['gender_targeting']

# Get the impressions from the highest spend row.
impressions = highest_spend_row['impressions']

# Get the objective from the highest spend row.
objective = highest_spend_row['objective']

# Get the optimization_goal from the highest spend row.
optimization_goal = highest_spend_row['optimization_goal']

### PRINT VALUES ###

# Print the results with the currency type before the spend value.
print(f"The ad with the highest spend is{ad_name} with a spend of{currency_type}{spend}.")

# Print the ad_format_asset.
print(f"The ad format for this ad is{ad_format_asset}.")

# Print the target demographic.
print(f"The target demographic for this ad was between{age_targeting} years old.")

# Print the clicks and conversions.
print(f"The ad received {clicks} clicks, with {conversions} of those clicks leading to conversions.")

# Print the cost_per_ad_click and cost_per_conversion.
print(f"This ad cost{currency_type}{cost_per_ad_click} per ad click, and cost{currency_type}{cost_per_conversion} per conversion.")

# Print the DMA, gender_targeting and age_targeting.
print(f"The designated market area (DMA) for this ad was{dma}, and primarily targeted{gender_targeting}s in the{age_targeting} age range.")

# Print the impressions.
print(f"This ad received {impressions} impressions.")

# Print the objectives and optimization_goal.
print(f"The objective of this ad was{objective}, and the optimisation goal was{optimization_goal}.")