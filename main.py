import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Excel Data
# -----------------------------
file_path = "energy_data.xlsx"  # Excel file path
data = pd.read_excel(file_path)

hours = data["Hour"].to_numpy()
energy_consumption = data["Energy_Consumption"].to_numpy()

# -----------------------------
# 2. Numerical Analysis (NumPy)
# -----------------------------
average_consumption = np.mean(energy_consumption)
max_consumption = np.max(energy_consumption)
min_consumption = np.min(energy_consumption)
peak_hour = np.argmax(energy_consumption)

print("Average Energy Consumption:", round(average_consumption, 2), "kWh")
print("Maximum Energy Consumption:", max_consumption, "kWh")
print("Minimum Energy Consumption:", min_consumption, "kWh")
print("Peak Load Hour:", peak_hour, ":00 hrs")

# -----------------------------
# 3. Line Plot – Hourly Consumption
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(hours, energy_consumption, marker='o')
plt.title("Hourly Energy Consumption")
plt.xlabel("Hour of Day")
plt.ylabel("Energy Consumption (kWh)")
plt.grid(True)
plt.show()

# -----------------------------
# 4. Bar Chart – Load Distribution
# -----------------------------
plt.figure(figsize=(10, 5))
plt.bar(hours, energy_consumption)
plt.title("Energy Load Distribution by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Energy Consumption (kWh)")
plt.show()

# -----------------------------
# 5. Peak Load Highlight
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(hours, energy_consumption, marker='o')
plt.scatter(hours[peak_hour], energy_consumption[peak_hour])
plt.text(
    hours[peak_hour],
    energy_consumption[peak_hour] + 5,
    "Peak Load",
    ha='center'
)
plt.title("Peak Energy Demand Identification")
plt.xlabel("Hour of Day")
plt.ylabel("Energy Consumption (kWh)")
plt.grid(True)
plt.show()