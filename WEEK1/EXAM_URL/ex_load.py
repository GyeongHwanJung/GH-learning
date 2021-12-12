import urllib.request as req     #웹에서 데이터 파일 수집용 모듈
import os.path                   #폴더, 파일 관리 모듈


URL = "http://api.aoikujira.com/ip/ini"
DIR = "../Data/"
SAVE_NAME = DIR+"ini.txt"

if not os.path.exists(DIR): os.mkdir(DIR)

res=req.urlopen(URL)             #HTTPResponse 객체
data=res.read()                  #HTTPResponse 객체에서 데이터만 읽기

#데이터 확인하기
print('type(data) =', type(data))
print(data)

text=data.decode("utf-8")
print('\ntype(text) =', type(text))
print(text)

with open(SAVE_NAME, mode="w", encoding='utf-8') as f:
    f.write(text)

print("Save OK") if os.path.exists(SAVE_NAME) else print("Save Fail")