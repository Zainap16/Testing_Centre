import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='dpg-cokgiiv79t8c73ca77kg-a',
    port='5432',
    dbname='matric',
    user='matric_user',
    password='YlFGQ4TUvdU6937gns6IUdflTGoDnvmk'
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
