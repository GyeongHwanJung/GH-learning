# ----------------------------------------------------------
# 로지스틱회귀 실습 By Keras
# 0과 1로 분류  => 이진분류기
# ----------------------------------------------------------
# 모듈 로딩 --------------------------------------------
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import matplotlib.pyplot as plt

# (1) 데이터 준비 ----------------------------------------
X=[1,2,3,4,5,6,7,8,9]           # 공부 시간
y=[0,0,0,0,1,1,1,1,1]           # 합격 여부

# (2) 모델 구성 & 생성 ----------------------------------------
model = Sequential()

# 입력 x의 차원은 1, 출력 y의 차원도 1 ==> 회귀
# activation = 'sigmoid'
model.add(Dense(1, input_dim=1, activation='sigmoid'))

# sgd는 경사 하강법을 의미. 학습률(learning rate, lr)은 0.01.
sgd = optimizers.SGD(lr=0.5)

# 손실 함수(Loss function)은  binary_crossentropy 사용
model.compile(optimizer=sgd ,
              loss='binary_crossentropy',
              metrics=['mse'])

# (3) 학습 ----------------------------------------
# 주어진 X와 y데이터에 대해서 오차를 최소화하는 작업을 300번 시도
model.fit(X,y, batch_size=1, epochs=300, shuffle=False)

# (4) 검증 및 시각화 ------------------------------
plt.plot(X, model.predict(X), 'b', X,y, 'ro')
plt.show()

# (5) 테스트  ------------------------------
print(f"[9.5] => {model.predict([9.5])}")