import urllib.request
import urllib.parse
import os.path

API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
VALUES = { 'stnId' : '108' }
DIR = "../Data/"

params=urllib.parse.urlencode(VALUES)
print("params=", params)

url=API+"?"+params
print("url=", url)

data=urllib.request.urlopen(url).read()
text=data.decode("utf-8")
print(text)

if not os.path.exists(DIR): os.mkdir(DIR)

with open('../Data/forecast.txt', mode="w", encoding='utf-8') as f:
        f.write(text)

print("Save OK") if os.path.exists('../Data/forecast.txt') else print("Save Fail")