import requests

API_KEY = "54fba3301d4ac44db4a66082938d4466"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
params = {"q": city, "appid": API_KEY, "units": "metric"}
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"{city} Weather: {temp}°C, {desc}")
else:
    print("City not found or API failed.")
