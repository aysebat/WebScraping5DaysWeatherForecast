
from datetime import datetime
import requests
import pprint


apikey = '4429faaaa08bd6135bd6b3c567c46811'
lat =44.34
lon =10.99
url = f"https://api.openweathermap.org/data/2.5/forecast?lat=57&lon=-2.15&cnt=100&appid={apikey}&units=imperial"


r =  requests.get(url)
requested_json = r.json()
pprint.pprint(requested_json['city']['name'])

count_of_list= len(requested_json['list'])
time_of_weather =[]
for i in range(count_of_list):
  get_item = requested_json['list'][i]['dt']
  convert_time = datetime.fromtimestamp(get_item).strftime('%Y-%m-%d %H:%M:%S')
  temperature = requested_json['list'][i]['main']['temp']
  print(temperature)
  description = requested_json['list'][i]['weather'][0]['description']
  print(description)
  print( convert_time)

print("Whole Data")
pprint.pprint(requested_json)

#pprint.pprint(requested_json['list'])