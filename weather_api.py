import requests
city_name = "Delhi"
apiKey = "ca48f74c00fc1ba1e6f86999e6462258"
apiUrl = f'https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${apiKey}&units=metric'

response = requests.get(apiUrl)
data = response.json()  
print(data)


