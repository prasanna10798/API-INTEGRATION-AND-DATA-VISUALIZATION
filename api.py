import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import pandas as pd

API_KEY = "caf7119e1321e53a6b1addea732e6fca"
CITY = "Chennai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

weather_data = []

for item in data["list"]:
    dt = datetime.datetime.fromtimestamp(item["dt"])
    temp = item["main"]["temp"]
    humidity = item["main"]["humidity"]
    weather = item["weather"][0]["main"]

    weather_data.append({
        "DateTime": dt,
        "Temperature (°C)": temp,
        "Humidity (%)": humidity,
        "Weather": weather
    })

df = pd.DataFrame(weather_data)

sns.set(style="whitegrid")plt.figure(figsize=(12, 6))
plt.plot(df["DateTime"], df["Temperature (°C)"], color="tomato", marker="o")
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(x="DateTime", y="Humidity (%)", data=df, marker="o", color="dodgerblue")
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 5))
sns.countplot(x="Weather", data=df, palette="Set2")
plt.title(f"Weather Conditions Count in Forecast for {CITY}")
plt.xlabel("Weather Type")
plt.ylabel("Count")
plt.show()

print("\n🌦️ Weather data fetched and visualizations generated successfully!")
