# ----------------------------------------------------------
# 선형회귀 실습  ==> y =wx+b
# ----------------------------------------------------------
# 모듈 로딩 --------------------------------------------------
from tensorflow.keras.models import Sequential   # 모델 바운딩 모듈
from tensorflow.keras.layers import Dense        # 전결합층 모듈
from tensorflow.keras import optimizers          # 최적화 모듈
import matplotlib.pyplot as plt                  # 데이터 시각화 모듈

# (1) 데이터 준비 --------------------------------------------
X=[1, 2, 3, 4, 5, 6, 7, 8, 9]                   # 공부 시간
y=[11, 22, 33, 44, 53, 66, 77, 87, 95]          # 성적

# (2) 모델 구성 & 생성 ----------------------------------------
model = Sequential()

# 입력 x의 차원은 1, 출력 y의 차원도 1 ==> 선형 회귀
# 출력노드 갯수, 입력 데이터 갯수, activation = 'linear'
model.add( Dense(1, input_dim=1, activation='linear') )

# sgd 경사 하강법 / 학습률(learning rate, lr) : 0.01.
sgd = optimizers.SGD(lr=0.01)

# 모델 생성 ----------------------------------------
model.compile(optimizer=sgd ,
              loss='mse',
              metrics=['accuracy'])

# (3) 학습 ----------------------------------------
# 주어진 X와 y데이터에 대해서 오차 최소화 작업 300번 시도
model.fit(X,y, batch_size=1, epochs=300, shuffle=False)

# (4) 검증 및 시각화 -------------------------------
plt.plot(X, model.predict(X), 'b', X, y, 'ro')
plt.show()

# (5) 테스트  -------------------------------------
print(f"[9.5] => {model.predict([9.5])}")