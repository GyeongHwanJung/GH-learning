import requests
import json

apikey="4ffa1fe608d6489a4e15ce7c9aadde3f"

cities=["Seoul,KR","Tokyo,JP","New York,US"]

api="https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

k2c=lambda k: k-273.15

for name in cities:
    url=api.format(city=name, key=apikey)
    print("url : ", url)

    r = requests.get(url)
    data = json.loads(r.text)
    print("type(data) : ", type(data))

    print("+ 도시 =", data["name"])
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 최저 기온 =", k2c(data["main"]["temp_min"]))
    print("| 최고 기온 =", k2c(data["main"]["temp_max"]))
    print("| 습도 =", k2c(data["main"]["humidity"]))
    print("| 기압 =", k2c(data["main"]["pressure"]))
    print("| 풍향 =", k2c(data["wind"]["deg"]))
    print("| 풍속 =", k2c(data["wind"]["speed"]))
    print("")
