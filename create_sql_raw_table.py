import pandas as pd
import psycopg2
from psycopg2.extensions import AsIs

# Read the CSV file
data = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Create a connection to the database
conn = psycopg2.connect(database="data", user="root", password="root", host="localhost", port="5432")

# Create a cursor
cursor = conn.cursor()

# Get the column names and types from the CSV file
columns = data.columns.tolist()
column_types = ['text' if dtype == 'object' else 'numeric' for dtype in data.dtypes]

# Create a table with the same column names and data types as the CSV file
create_table_query = 'CREATE TABLE fb_ad_insight_api_transpose (%s)'
column_names = [f'"{column}"' for column in columns]
cursor.execute(create_table_query, [AsIs(','.join([f'{name} {data_type}' for name, data_type in zip(column_names, column_types)]))])

# Insert the data into the table
for _, row in data.iterrows():
    row_values = row.values.tolist()
    insert_query = 'INSERT INTO mytable (%s) VALUES %s'
    cursor.execute(insert_query, (AsIs(','.join(column_names)), tuple(row_values)))

# Commit the changes and close the connection
conn.commit()
conn.close()
