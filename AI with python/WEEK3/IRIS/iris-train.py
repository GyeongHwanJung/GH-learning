# 모듈로딩 -----------------------------------------------
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import urllib.request as req
import os.path

# 데이터변수 선언 ----------------------------------------
CSV_DIR  ='../Data/IRIS/'
CSV_FILE = CSV_DIR+'iris.csv'

# (2) 붓꽃 CSV 데이터 준비 ------------------- -----------
csv = pd.read_csv(CSV_FILE)
print('type(csv) =>', type(csv))

# 필요한 데이터(column) 추출 ------------------------------
csv_data  = csv[["sepal.length","sepal.width","petal.length","petal.width"]]
csv_label = csv["variety"]

# 학습 데이터와 테스트 전용 데이터 분류 ----------------------
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

# (3) 데이터 학습 & 예측 ---------------------------------
clf = svm.SVC()
clf.fit(train_data, train_label)    # 학습

# (4) 데이터 테스트 --------------------------------------
pre = clf.predict(test_data)        # 테스트
print('type(clf)=', type(clf))

# (5)정확도 검사 -----------------------------------------
ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 =", ac_score)

# (6) 4개 값을 입력 받아서 iris 판별 테스트 ---------------
data=list(map(float, input("Enter sl, sw, pl, pw : ").split()))
print("indata => ", data)
new_data=[]
new_data.append(data)
print("new_data => ", new_data)

pre = clf.predict(new_data)        # 테스트
print(f'{new_data} ==> ', pre)

