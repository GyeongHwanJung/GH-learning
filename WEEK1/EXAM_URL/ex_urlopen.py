import urllib.request as req
import os.path


URL = "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
DIR="../Image/"
SAVE_NAME=DIR+"google2.png"
DEBUG = True

if not os.path.exists(DIR): os.mkdir(DIR)

resObj = req.urlopen(URL)
header = resObj.getheaders()
data = resObj.read()

if DEBUG:
    print('type(resObj) => ',type(resObj))
    print('resObj.headers() => \n', header)
    print('resObj.read() => \n', data)

#text=data.decode("utf-8")       #텍스트 데이터가 아님
#print(f"text => {text}")

with open(SAVE_NAME, mode='wb') as file:
    file.write(data)

print("저장!") if os.path.exists(SAVE_NAME) else print("저장 실패!")