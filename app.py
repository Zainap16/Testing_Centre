import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import psycopg2
import os

# Load environment variables from .env file
load_dotenv()

# Get database connection details from environment variables
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Create a cursor object
cursor = conn.cursor()

# Read data from Excel spreadsheet
data = pd.read_excel("results.xlsx")

# Prepare data for pie chart
labels = ["Unemployed", "Employed"]
sizes = [data["Unemployed"].sum(), data["Employed"].sum()]
colors = ["lightcoral", "lightskyblue"]
explode = (0, 0.1)

# Create pie chart
plt.title("Unemployed VS Employment")
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.axis("equal")

# Insert data into PostgreSQL table
for index, row in data.iterrows():
    cursor.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (row['Unemployed'], row['Employed']))

# Commit changes and close cursor and connection
conn.commit()
cursor.close()
conn.close()

# Display the pie chart
plt.show()
