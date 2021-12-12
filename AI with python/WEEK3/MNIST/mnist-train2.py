# 모듈로딩 ------------------------------------------
import joblib
from sklearn import svm, metrics
import pandas as pd

# 데이터 변수 선언 ----------------------------------------
TRAIN_FILE = "../Data/MNIST/train.csv"
TEST_FILE = "../Data/MNIST/t10k.csv"
SAVE_FILE = "../Data/MNIST/handdigit.pkl"
DEBUG = True

# (1)학습 및 테스트용 데이터 로딩 -----------------------
data=pd.read_csv(TRAIN_FILE, header=None)
test=pd.read_csv(TEST_FILE,  header=None)
# print(f'data.describe() =>\n {data.describe()}')
# print(f'data.head() =>\n {data.head()}')
# data.info()
#
# print(f'data.iloc[:, 1:] =>\n {data.iloc[:, 1:].head()}')
# print(f'data.iloc[:, 0] =>\n {data.iloc[:, 0].head()}')

# 데이터 정규화 ( 값의 범위를 0 ~ 1 사이)
# 학습 데이터와 테스트 전용 데이터 분류 ----------------------
train_data = data.iloc[:, 1:]/256
train_label = data.iloc[:, 0]

test_data = test.iloc[:, 1:]/256
test_label = test.iloc[:, 0]

# # (2) 학습하기 --------------------------------------
clf = svm.SVC()
clf.fit(train_data, train_label)

# (3) 예측하기 ---------------------------------------
predict = clf.predict(test_data)

# (4) 결과 확인하기 -----------------------------------
# 분류 성능
ac_score = metrics.accuracy_score(test_label, predict)
print("정답률 =", ac_score)

# 분류 리포트
cl_report = metrics.classification_report(test_label, predict)
print("리포트 ---------------\n" , cl_report)

# (5) 학습 데이터 저장 ------------------------------------
SAVE_FILE = "../Data/MNIST/handdigit.pkl"

if ac_score*100 >= 98:
    # 모델 저장하여 파일로 생성
    joblib.dump(clf, SAVE_FILE)
    print("Model SAVE OK")


# # 테스트 -------------------------------------------------
# # https://convertio.co/kr/jpg-pgm/
# img_data=[]
# with open("../Data/MNIST/PGM/my_07.pgm", mode='rb') as fp:
#     #data=fp.read(len("P2 28 28 255\n"))
#     fp.seek(len("P2 28 28 255\n"))
#
#     while True:
#         data=fp.read(1)
#         if not data: break
#         img_data.append(struct.unpack('>B', data)[0])
#         print(f"data => {data}")
#         print(f"img_data => {img_data}")
#
# # print(len("P2 28 28 255\n"))
# # print(f" pgm data = > {len(data)}")
# # print(f" type(data)= > {type(data)}, {type(data.decode('utf-16'))}")
# # data16= list(data.decode('utf-16'))
# # print(data16)
# # img_data = struct.unpack('f', data)
# print(f"img_data => {len(img_data)}\n{img_data}")
# print(f"img_data => {[ n/256 for n in img_data ]}")
#
# predict = clf.predict([[ n/256 for n in img_data ]])
# print(f"New Data predict => {predict}")