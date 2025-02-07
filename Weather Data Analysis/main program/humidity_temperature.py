import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("weather_data.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Identify High Humidity Days (Humidity > 80%)
high_humidity_days = df["Humidity (%)"] > 80

# Create Plot
plt.figure(figsize=(12, 5))

# Plot Humidity
plt.plot(df["Date"], df["Humidity (%)"], marker="o", linestyle="-", 
         color="blue", alpha=0.6, label="Humidity (%)")

# Highlight High Humidity Days in Green
plt.scatter(df["Date"][high_humidity_days], df["Humidity (%)"][high_humidity_days], 
            color="red", label="High Humidity (>80%)", zorder=3)

# Labels & Titles
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.title("Humidity Trends Over 6 Months")

# Improve X-axis Date Formatting
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)

# Add Legend Outside to Prevent Overlap
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Save the Plot (Optional)
plt.savefig("humidity_plot.png", dpi=500, bbox_inches='tight')

# Show Plot
plt.show()
