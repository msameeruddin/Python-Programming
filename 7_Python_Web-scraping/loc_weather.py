import requests

class WeatherApp():
    def __init__(self, location):
        self.location = location.lower()
        self.ip_url = "http://ip-api.com/json"
        self.apikey = "9d41bd4e5bffd04e03a6cb6832066559"
        self.weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        ###################
        self.weather_data = self.get_weather_data()
        self.lat = self.weather_data['coord']['lat']
        self.lon = self.weather_data['coord']['lon']

    def get_default_location(self):
        default_loc_req = requests.get(url=self.ip_url)
        default_loc_data = default_loc_req.json() if default_loc_req.status_code == 200 else {}
        default_loc = default_loc_data['city']
        return default_loc
    
    def get_weather_data(self):
        weather_loc_url = self.weather_url.format(self.location, self.apikey)
        weather_loc_req = requests.get(url=weather_loc_url)
        
        if weather_loc_req.status_code == 200:
            weather_data = weather_loc_req.json()
        else:
            self.location = self.get_default_location()
            weather_loc_url = self.weather_url.format(self.location, self.apikey)
            weather_loc_req = requests.get(url=weather_loc_url)
            weather_data = weather_loc_req.json()
        
        return weather_data

    def get_parsed_details(self):
        if self.weather_data:
            desc = self.weather_data['weather'][0]['description']
            temp = self.weather_data['main']['temp']
            celsius_temp = round(temp - 273, 2)
            farenheit_temp = round((celsius_temp * (9/5) + 32), 2)
            humidity = self.weather_data['main']['humidity']
            wind_speed = self.weather_data['wind']['speed']
            clouds = self.weather_data['clouds']['all']
        else:
            desc = None
            celsius_temp = None
            farenheit_temp = None
            humidity = None
            wind_speed = None
            clouds = None
        
        return [desc, celsius_temp, farenheit_temp, humidity, wind_speed, clouds]