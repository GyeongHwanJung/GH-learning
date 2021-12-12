# 모듈 로딩 ------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager as fm   # 한글 폰트 설정
import urllib.request as req
import os.path

# (1) 데이터 준비 -----------------------------------------------
DIR= "../Data/"
URL ="https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
FILE_NAME = DIR+"iris.csv"

if not os.path.exists(DIR): os.mkdir(DIR)
req.urlretrieve(URL, FILE_NAME)


# Pandas로 CSV 데이터 파일 가져오기 -----------------------
tbl = pd.read_csv("../Data/iris.csv", index_col=4)

# (2) 그래프 그리기 -----------------------------------------
# 한글 설정
font_path = r'C:\Windows\Fonts\malgun.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
plt.rc('font', family=font_name)     # mpl.rcParams['font.family'] = 'Gullim'
plt.rc('axes', unicode_minus=False)  # mpl.rcParams['axes.unicode_minus'] = False

# 분포도 그래프 그리기
print("columns => ", tbl.columns)
print("index   => ",  tbl.index)

plt.scatter(tbl.loc['Setosa']["petal.length"],    tbl.loc['Setosa']["petal.width"],        c='red',      label='Setosa')
plt.scatter(tbl.loc['Versicolor']["petal.length"], tbl.loc['Versicolor']["petal.width"],   c='yellow',   label='Versicolor')
plt.scatter(tbl.loc['Virginica']["petal.length"],  tbl.loc['Virginica']["petal.width"],    c='blue',     label='Virginica')

# 범례, 라벨 출력 및 저장
plt.legend()
plt.ylabel('PetalLength')
plt.xlabel('PetalWidth')
plt.show()