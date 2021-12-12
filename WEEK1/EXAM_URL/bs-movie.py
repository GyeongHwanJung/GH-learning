#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

from bs4 import BeautifulSoup
import urllib.request as req

MURL = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
FURL = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

res=req.urlopen(MURL)
print(type(res))

soup=BeautifulSoup(res,"html.parser")

movies=soup.select("#old_content > table > tbody > tr > td.title > div > a")
print("movies={}, \nlen={}".format(movies, len(movies)))

res=req.urlopen(FURL)
soup=BeautifulSoup(res,"html.parser")
USD=soup.select("#exchangeList > li.on > a.head.usd > div > span.value")
print(type(USD), USD, USD[0].string)

for idx, item in enumerate(movies, start=1):
    print(idx, item.string)

#print("movie.attrs['title'] = ", movie.attrs['title'])
#print("movie = ", movie.string)