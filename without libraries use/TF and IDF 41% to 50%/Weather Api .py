import requests

api_key = "YOUR_API_KEY"
city = "Lucknow"

url = f"https://api.openweathermap.org/data/2.5/forecast?q=Varanasi&appid=4a1f8a61b74546825af1e0be106e797b"

response = requests.get(url)
print(response.json())