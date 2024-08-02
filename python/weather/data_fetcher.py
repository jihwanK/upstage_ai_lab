import requests

class DataFetcher:
    def __init__(self, API_KEY, city):
        self.api_key = API_KEY
        self.city = city
    
    def fetch_weather(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"
        res = requests.get(url)
        data = eval(res.content)
        return data
    