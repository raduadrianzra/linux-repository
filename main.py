import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=44.43&longitude=26.10&current_weather=true"

response = requests.get(url)


data = response.json()


temperatura = data['current_weather']['temperature']
print(f"Temperatura curentă în București este: {temperatura} °C")
