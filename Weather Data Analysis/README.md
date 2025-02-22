# 📌 Weather Data Analysis with NumPy & Matplotlib

This project analyzes **weather data** (temperature, humidity, and rainfall) using **NumPy, Pandas, and Matplotlib**. It provides **statistical insights and visualizations** for a **6-month period**.

---

Weather Data Analysis

## 📂 Project Structure

```
Weather Data Analysis  
├── 📁 main_program                   # Contains Python scripts for analysis  
│   ├── main.py                        # Main script for data processing & visualization  
│   ├── humidity_temperature.py        # Analyzes humidity and temperature together  
│   ├── rainfall_visualizations.py     # Analyzes & plots rainfall data  
│   ├── rainfall_temperature.py        # Analyzes rainfall & temperature trends together  
│   ├── temperature_visualizations.py  # Analyzes & plots temperature trends  
│  
├── 📁 plotting_images                 # Contains all saved plots  
│   ├── humidity_plot.png               # Humidity visualization  
│   ├── rainfall_plot.png               # Rainfall visualization  
│   ├── temperature_plot.png            # Temperature visualization  
│   ├── temperature_rainfall_plot.png   # Combined temperature & rainfall visualization  
│  
├── 📁 jupyter_lab                      # Contains Jupyter Notebook versions of the scripts  
│   ├── weather_data.ipynb  
│   ├── temperature_visualizations.ipynb  
│   ├── rainfall_visualizations.ipynb  
│   ├── humidity_visualizations.ipynb  
│   ├── temperature_rainfall_visualizations.ipynb  
│  
├── weather_data.csv                     # Weather dataset (Temperature, Humidity, Rainfall)  
├── README.md                            # Project documentation  
```


## 🚀 Features  

✔ **Data Processing**: Reads CSV data and converts it into NumPy arrays for analysis.  
✔ **Statistical Analysis**: Computes **mean, median, min, and max** values for weather parameters.  
✔ **Temperature Trends**: Identifies **heatwave days (>40°C)** and highlights them in red.  
✔ **Rainfall Analysis**: Marks **dangerous rainfall days (>30mm)** in red.  
✔ **Humidity Trends**: Analyzes humidity variations.  
✔ **Visualizations**: Uses **Matplotlib** to generate clear and customized plots.  
✔ **Data Export**: Saves analyzed plots in the **plotting_images/** folder.  

---

## 📊 Generated Plots  

✅ **Temperature Trends** → `temperature_plot.png`  
✅ **Rainfall Trends** → `rainfall_plot.png`  
✅ **Humidity Trends** → `humidity_plot.png`  
✅ **Temperature & Rainfall Combined Trends** → `temperature_rainfall_plot.png`  

All plots are saved inside the **plotting_images/** folder.  

---

## 📦 Installation & Usage  

### 🔹 Requirements  
Make sure you have Python installed along with the required libraries:  
```
pip install numpy pandas matplotlib
🔹 Running the Analysis
1️⃣ Navigate to the main_program/ folder:
2️⃣ Run the script:




📌 Developed by: Prakash Pandey 😊




