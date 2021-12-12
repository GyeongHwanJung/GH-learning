from urllib.parse import urlparse, urlsplit, urlencode

data = urlparse("http://example.com/html/a.html?name=123")
print( f"data => {data}")
print( f"scheme => {data.scheme}")
print( f"netloc => {data.netloc}")
print( f"path => {data.path}")
print( f"params => {data.params}")
print( f"query => {data.query}")
print( f"fragment => {data.fragment}")

data2=urlsplit("http://example.com/html/a.html?name=123")
print( f"data2 => {data2}")

url=urlencode({'name':'홍길동'})
print(url)

url=urlencode({'name':'Hong'})
print(url)