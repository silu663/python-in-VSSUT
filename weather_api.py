import requests
apiKey = "ca48f74c00fc1ba1e6f86999e6462258"
city_name = "Delhi"

url = f"https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${apiKey}&units=metric"
response = requests.get(url)

print(response.status_code)   # 200 means success
print(response.json())    

