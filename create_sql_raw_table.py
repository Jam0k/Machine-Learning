import pandas as pd
import psycopg2
from psycopg2.extensions import AsIs

# Read the CSV file
data = pd.read_csv('fb_ad_insight_api_transpose.csv')

# Create a connection to the database
conn = psycopg2.connect(database="data", user="root", password="root", host="localhost", port="5432")

# Create a cursor
cursor = conn.cursor()

# Get the column names and data types from the CSV file
columns = data.columns.tolist()
column_types = [str(dtype) for dtype in data.dtypes.tolist()]

# Create a table with the same column names and data types as the CSV file
create_table_query = 'CREATE TABLE mytable (%s)'
cursor.execute(create_table_query, [AsIs(','.join([f'{column} {column_type}' for column, column_type in zip(columns, column_types)]))])

# Insert the data into the table
for _, row in data.iterrows():
    row_values = row.values.tolist()
    insert_query = 'INSERT INTO mytable (%s) VALUES %s'
    cursor.execute(insert_query, (AsIs(','.join(columns)), tuple(row_values)))

# Commit the changes and close the connection
conn.commit()
conn.close()
