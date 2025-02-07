import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("weather_data.csv")
numpy_data = df.to_numpy()

Rainfall = numpy_data[:,3]

df["Date"] = pd.to_datetime(df["Date"])
plt.figure(figsize=(12,5))
plt.plot(df["Date"],Rainfall,label = "Rainfall (mm)",marker = 'o', linestyle="-")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.title("Rainfall Trends Over 6 Months")
plt.legend()
plt.xticks(rotation=45)
plt.show()