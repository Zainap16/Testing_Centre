import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Connect to the Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=test.accdb;'
)
conn = pyodbc.connect(conn_str)

# Query the data from the database
query = "SELECT * FROM this_one"
data = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Prepare data for pie chart
labels = ["Unemployed", "Employed"]
sizes = [data["Unemployed"].sum(), data["Employed"].sum()]
colors = ["lightcoral", "lightskyblue"]
explode = (0, 0.1)

# Create pie chart
plt.title("Unemployed VS Employment")
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
