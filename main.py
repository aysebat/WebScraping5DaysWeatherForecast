
from datetime import datetime
import requests
import pprint


def get_weather_forecast(lat=57, lon=-2.15, apikey = '4429faaaa08bd6135bd6b3c567c46811', units='imperial'):
  """get the weahter forecast for the next 5 day for each3 hours
      lat: latitude of the city
      lon:longitude of the city
      apikey: apikey from openweathermap
      units:get the Celcuis degree for temperature
      You may change the defination and get the new data results  
  """
  
  url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt=100&appid={apikey}&units={units}"
    
  r =  requests.get(url)
  requested_json = r.json()
  city = requested_json['city']['name']
  name_of_data = f"data_{city}_{datetime.today()}"
  print(f"{name_of_data}.txt file created")
  with open(f"{name_of_data}.txt","a") as file:
    for object in requested_json['list']:
      #loop over the content list element
      #city = requested_json['city']['name']
      get_item = object['dt']
      time_w = datetime.fromtimestamp(get_item).strftime('%Y-%m-%d %H:%M:%S')
      temperature= object['main']['temp']
      description = object['weather'][0]['description']
  
      file.write(f"{city },{time_w},{temperature},{description}\n")
    
get_weather_forecast()