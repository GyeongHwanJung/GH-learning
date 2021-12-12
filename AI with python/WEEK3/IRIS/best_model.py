# --------------------------------------------------
# 모델별 다양한 모델 적용 후 최고 정확도 모델 찾기
# --------------------------------------------------
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.utils import all_estimators

BASIC = False

if BASIC:
    # 필터별로 모델 리스트 출력 ------------------------------
    estimators = all_estimators(type_filter='classifier')
    all_regs = []
    for name, ClassifierClass in estimators:
        try:
            all_regs.append(name)
        except Exception:
            pass

    #필터에 해당하는 모델 리스트 출력
    for model in all_regs: print(model)

# (1) 데이터 준비 ----------------------------------
iris = load_iris()      # scikit-learn dataset 활용
# 데이터(피쳐) & 라벨 분류
X1 = iris.data
y1 = iris.target
X1 = X1[:, :2]         # 꽃받침길이 & 너비 데이터만 사용

# (2) 모델링 --------------------------------------
estimators = all_estimators(type_filter='classifier')
all_esti = []
for name, ClassifierClass in estimators:
    try:
        # 모델별 학습 ---------------------
        clf = ClassifierClass()
        clf.fit(X1, y1)

        # 예측 & 검증 ---------------------
        y1_pred  = clf.predict(X1)
        ac_score = accuracy_score(y1, y1_pred)
        all_esti.append([name, round(ac_score, 2)])
    except Exception as e:
        pass

# 정확도가 가장 높은 모델 출력 ------------------------
all_esti.sort(key=lambda x:x[1], reverse=True)
for item in all_esti:
    print(item)