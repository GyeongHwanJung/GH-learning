# 모듈로딩 ------------------------------------------
from sklearn import svm, metrics
import joblib

# 데이터 변수 선언 ----------------------------------------
DEBUG = False

# [함수] 데이터 CSV 파일 읽기 및 가공 -------------------
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        # train.csv 파일에 있는 데이터 읽어서 데이터 셋 & 라벨 분리
        for line in f:
            cols = line.split(",")
            if DEBUG:
                print('len(cols) = {}'.format(len(cols)))
                print('cols data => {}'.format(cols))

            if len(cols) < 2: continue       # line 구분문자는 데이터가 아니므로 스킵

            labels.append(int(cols.pop(0)))  # 데이터 리스트에서 첫번째 요소 꺼내기 => 숫자 라벨
            vals = list(map(lambda n: int(n) / 256, cols))  # 784개 이미지 데이터 리스트로 변환
            images.append(vals)                             # 이미지 데이터 저장

    # 딕셔너리 티입으로 반환
    return {"labels":labels, "images":images}

# (1)학습 및 테스트용 데이터 로딩 -----------------------
data = load_csv("../../data/MNIST/train.csv")   # 딕셔너리 타입 학습   데이터 로딩
test = load_csv("../../data/MNIST/t10k.csv")    # 딕셔너리 타입 테스트 데이터 로딩

# (2) 학습하기 --------------------------------------
clf = svm.SVC(gamma='scale')
clf.fit(data["images"], data["labels"])

# (3) 예측하기 ---------------------------------------
predict = clf.predict(test["images"])

# (4) 결과 확인하기 -----------------------------------
ac_score  = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)

# 학습 데이터 저장하기
# joblib
joblib.dump(clf, "../../data/MNIST/handdigit.pkl")
print("SAVE OK")