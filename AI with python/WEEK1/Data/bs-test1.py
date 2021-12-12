from bs4 import BeautifulSoup

html="""
<html>
  <title>타이틀입니다.</title>
  <body>
  <h1 id='h11'>스크레이핑이란?</h1>
  <p id='p1'>웹 페이지를 분석하는 것</p>
  <p align='center' id='p2'>원하는 부분을 추출하는 것</p>
</body></html>
"""
DEBUG = True


soup=BeautifulSoup(html, 'html.parser')
if DEBUG: print(type(soup))

title = soup.html.title
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

h1=soup.find('h1')
h1_2=soup.find(id='h11')
print(f"h1 => {h1.string}, h1_2 => {h1_2.string}")

p1=soup.find('p')
p1_2=soup.find(id='p1')
print(f"p1 => {p1.string}, p1_2 => {p1_2.string}")

pall=soup.findAll('p')
print(f"pall =>{pall}, pall[0].string => {pall[0].string}")

print("title = " + title.string)
print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)
print("p2.attrs = ", p2.attrs)                      # 태그의 모든 속성 dict 타입
print("p2.attrs['align'] = ", p2.attrs['align'])