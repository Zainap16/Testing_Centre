import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("results.xlsx")

# prepare data for pie chart
labels = ["Unemployed","Employed"]
sizes = [data["Unemployed"].sum(), data["Employed"].sum()]
colors = ["lightcoral","lightskyblue"]

explode = (0,0.1)
#create pie chart
plt.title("Unemployed VS Employement")
plt.pie(sizes,labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.axis("equal")
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

















