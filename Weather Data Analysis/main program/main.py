import numpy as np
import pandas as pd

df = pd.read_csv("weather_data.csv")
# print(df)

numpy_data = df.to_numpy()
# print(numpy_data[:20])

# Temperature (°C)  Humidity (%)  Rainfall (mm) for notations

Temperature = numpy_data[:,1]
Humidity = numpy_data[:,2]
Rainfall = numpy_data[:,3]

print(Temperature)
print(Humidity)
print(Rainfall)

print("Mean Temperature :",round(np.mean(Temperature),5))
print("Median Temperature :",round(np.median(Temperature),5))
print("Max Temperature :",round(np.max(Temperature),5))
print("Min Temperature :",round(np.min(Temperature),5))

print("Mean Humidity:",round(np.mean(Humidity),5))
print("Median Humidity:",round(np.median(Humidity),5))
print("Max Humidity :",round(np.max(Humidity),5))
print("Min Humidity :",round(np.min(Humidity),5))

print("Mean Rainfall:",round(np.mean(Rainfall),5))
print("Median Rainfall:",round(np.median(Rainfall),5))
print("Max Rainfall :",round(np.max(Rainfall),5))
print("Min Rainfall :",round(np.min(Rainfall),5))


# Hot days
hot_days = numpy_data[Temperature>40]
print(f"Hot days :{hot_days}")

# #rainy days

rainy_days = numpy_data[Rainfall>30]
print(f"Rainy day :{rainy_days}")

# computing 7 day moving average for temperature
temp_moving_avg = np.convolve(Temperature,np.ones(7)/7,mode="valid")
print(temp_moving_avg)



