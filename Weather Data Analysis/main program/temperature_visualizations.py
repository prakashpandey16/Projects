import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv("weather_data.csv")
numpy_data = df.to_numpy()

temperature = numpy_data[:, 1]



# Convert date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(10, 4))
plt.plot(df["Date"], temperature, label="Temperature (°C)", marker='o', linestyle="-")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends Over 6 Months")
plt.legend()
plt.xticks(rotation=45)  # Rotate dates for better visibility
plt.show()
