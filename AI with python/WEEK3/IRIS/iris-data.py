# 모듈로딩 ---------------------------------------
from urllib import request
import os

# 데이터변수 선언 -----------------------------------
CSV_URL='https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
CSV_DIR  ='../Data/IRIS/'
CSV_FILE = CSV_DIR+'iris.csv'

# 붓꽃 데이터 파일 다운로드 ---------------------------------
if not os.path.exists(CSV_FILE):
    print("Download data")
    if not os.path.exists(CSV_DIR): os.mkdir(CSV_DIR)
    request.urlretrieve(CSV_URL, CSV_FILE)