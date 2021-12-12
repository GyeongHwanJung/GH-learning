# 모듈로딩
from urllib.request import urlretrieve
import os.path



URL="https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
DIR="../Image/"
FILE_NAME=DIR+"google.png"

if not os.path.exists(DIR): os.mkdir(DIR)

filename, header=urlretrieve(URL,FILE_NAME)
print(f"filename => {filename}")
print(f"header => {header}")
print("Save Ok")

