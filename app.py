import requests
import time

localtime = time.localtime(time.time())
city_input = input("Podaj nazwę miasta: ")
adress = 'http://api.openweathermap.org/data/2.5/weather?appid=8c1478e1474662cfbc44dd0c4a281a58&q={}'.format(city_input)
req = requests.get(adress).json()

weather = req["weather"][0]["main"]
temp = req["main"]["temp"]
wind = req["wind"]["speed"]
city = req["name"]
formatted_temp = int(temp - 273)
time = time.strftime("%Y-%m-%d", time.localtime())


print('{} in {} it is {} , the temperature is {}℃ and wind speed is {} m/s .'.format(time, city, weather, formatted_temp, wind))



