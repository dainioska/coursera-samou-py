import pprint
import requests
from dateutil.parser import parse

class YahooWeatherForecast:
    def get(self, city):
        url = 'https://query.yahooapis.com/v1/public/yql?q'
        data = requests.get(url).json()
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"])
                "high_temp": day_data["high"]
            })
        return forecast

class CityInfo:
    def __init__(self, city):
        self.city = city

    def weather_forecast(self):
        pass    
 


def _main():
    city_info = CityInfo("Vilnius")
    forecest = city_info.weather_forecat()
    pprint.pprint(forecest)


if __name__ == "__main__":
    _main()
        