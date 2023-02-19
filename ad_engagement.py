import pandas as pd
import matplotlib.pyplot as plt


# Read in the data
data = pd.read_csv("ad_engagement.csv")

# Print the number of rows and columns in the data
print("Number of rows:", len(data))
print("Number of columns:", len(data.columns))

# Print the number of unique values in each categorical column
categorical_cols = ["placement", "creative", "age", "gender", "location"]
for col in categorical_cols:
    num_unique = len(data[col].unique())
    print(f"Number of unique values in {col}: {num_unique}")

# Print the mean, median, and standard deviation of the engagement, conversions, cost_per_action, and cost_per_conversion columns
output_cols = ["engagement", "conversions", "cost_per_action", "cost_per_conversion"]
for col in output_cols:
    mean_val = data[col].mean()
    median_val = data[col].median()
    std_val = data[col].std()
    print(f"{col} statistics:")
    print(f"Mean: {mean_val:.2f}")
    print(f"Median: {median_val:.2f}")
    print(f"Standard deviation: {std_val:.2f}")