#=============================================
# Scikit-learn LinearRegression - Boston House
# =============================================

# 모듈 로딩 ------------------------------------
from sklearn import model_selection                 # 데이터 분류
from sklearn.linear_model import LinearRegression   # 모델
from sklearn import metrics                         # 검증
from sklearn import datasets                        # 데이터 셋

# 데이터 준비 -----------------------------------
# (1) 데이터 로딩 & x, y 데이터 분류
boston_dataset = datasets.load_boston()
x_data = boston_dataset.data
y_data = boston_dataset.target

# (2) 학습용 문제-라벨 & 테스트용 문제-라벨 데이터 분리
x_train, x_test, y_train, y_test =\
    model_selection.train_test_split(x_data, y_data, test_size=0.3)

print(f"x_train = {len(x_train)}, x_test = {len(x_test)}")

# 모델링 ------------------------------------
# (1) 학습 모델 객체 생성
model = LinearRegression()

# (2) 학습 => a(또는 w), b 값 추출
model.fit(x_train, y_train)

# (3) 테스트 y=ax+b <- x_train
y_predict = model.predict(x_train)

# (4) 성능 평가
score = metrics.r2_score(y_train, y_predict)
print(f" Train score => {score}")

# (5) 테스트형 데이터 기반 성능 평가
y_predict = model.predict(x_test)
score = metrics.r2_score(y_test, y_predict)
print(f" Test score => {score}")

# 가중치(w), 절편(b) 확인 ----------------------------------------------------
print(f"model.coef_ : \n{model.coef_}\n")
print(f"model.intercept_ :{model.intercept_}")
print(f"y={model.coef_}x+{model.intercept_}")