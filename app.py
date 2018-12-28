import requests
import time

localtime = time.localtime(time.time())
city_input = input("Podaj nazwę miasta: ")
adress = "http://api.openweathermap.org/data/2.5/weather?appid=8c1478e1474662cfbc44dd0c4a281a58&q=" + city_input
req = requests.get(adress).json()
weather = req["weather"][0]["main"]
temp = req["main"]["temp"]
wind = req["wind"]["speed"]
city = req["name"]

plik = open("Pogoda.txt", "w")
plik.write("Dnia " + time.strftime("%Y-%m-%d", time.localtime()) + " w mieście " + city + " temperatura wynosi " + str(temp) + " stopni Fahrenheita, a wiatr wieje z prędkością " + str(wind) + " m/s .")
plik.close()

print("Wykonano")
