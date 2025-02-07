import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
df = pd.read_csv("weather_data.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Identify Heatwave Days (Temperature > 40°C)
heatwave_days = df["Temperature (°C)"] > 40

# Identify Dangerous Rainfall Days (Rainfall > 30mm)
dangerous_rainfall = df["Rainfall (mm)"] > 30

# Create Subplots (Two Separate Plots)
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# ==== Temperature Plot ====
ax[0].plot(df["Date"], df["Temperature (°C)"], marker="o", linestyle="-", 
           color="orange", alpha=0.6, label="Temperature (°C)")

# Highlight Heatwave Days in Red
ax[0].scatter(df["Date"][heatwave_days], df["Temperature (°C)"][heatwave_days], 
              color="red", label="Heatwave (>40°C)", zorder=3)

# Labels & Titles
ax[0].set_ylabel("Temperature (°C)")
ax[0].set_title("Temperature Trends")
ax[0].legend(loc="upper left", bbox_to_anchor=(1, 1))  # Move legend outside
ax[0].grid(True, linestyle="--", alpha=0.5)

# ==== Rainfall Plot ====
ax[1].plot(df["Date"], df["Rainfall (mm)"], marker="o", linestyle="-", 
           color="blue", alpha=0.6, label="Rainfall (mm)")

# Highlight Dangerous Rainfall in Red
ax[1].scatter(df["Date"][dangerous_rainfall], df["Rainfall (mm)"][dangerous_rainfall], 
              color="red", label="Dangerous Rainfall (>30mm)", zorder=3)

# Labels & Titles
ax[1].set_xlabel("Date")
ax[1].set_ylabel("Rainfall (mm)")
ax[1].set_title("🌧️ Rainfall Trends")
ax[1].legend(loc="upper left", bbox_to_anchor=(1, 1))  # Move legend outside
ax[1].grid(True, linestyle="--", alpha=0.5)

# Improve Readability
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent overlap

# Show Plot
plt.show()
