#=====================================================
# Scikit-learn LinearRegression 실습
# ===================================================
# 모듈 로딩 ------------------------------------------
import numpy as np                                  # 수치계산 모듈
import matplotlib.pyplot as plt                     # 그래프 모듈
from sklearn.linear_model import LinearRegression   # 선형회귀 모듈

# (1) 데이터 준비 -------------------------------------
x=np.array([2, 4, 6, 8, 10])
y=np.array([81, 89, 93, 91, 97])
print(f"x ==>\n{x}\n")
print(f"type(x)=> {type(x)}, x.shape =>{x.shape}")

# 2차원으로 변경
x=x.reshape(-1,1)    # (행, 열) -1은 열의 갯수에 맞추어 행 설정
print(f"x ==>\n{x}\n")
print(f"type(x)=> {type(x)}, x.shape =>{x.shape}")

# (2) 학습 모델 객체 생성 ----------------------------------
model= LinearRegression()       # 모델 객체 생성
model.fit(x, y)                 # 데이터 학습 후 모델 생성
print(f"W=>{model.coef_}\nb=>{model.intercept_}")

# (3) 예측 및 모델 성능평가 --------------------------------
y2=model.predict(x)             # 가설에 의한 예측값
print(f"y  => {y}")
print(f"y2 => {y2}")

# 생성된 가설 모델에 데이터 적용 후 성능평가
print("성능평가 model.score(x,y)=>", model.score(x,y))

# # 그래프 출력 -----------------------------------------
# plt.figure()
# plt.plot(x, y, 'ro')
# plt.plot(x, model.predict(x), 'b^')
# plt.plot(x, x*model.coef_+model.intercept_, 'r--')
# plt.title('[ Hour & Jumsu ]')
# plt.xlabel('Hour')
# plt.ylabel('JUMSU')
# plt.grid()
# plt.show()
#
