from keras.layers.core import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
import pandas as pd
from keras.utils import np_utils

# (1) 데이터 준비 --------------------------------------------------
# 붓꽃 데이터 읽어 들이기
iris_data = pd.read_csv("../Data/iris.csv", encoding="utf-8")

# 붓꽃 데이터를 레이블과 입력 데이터로 분리
iris_data['variety'].replace({'Setosa':0,'Versicolor':1,'Virginica':2}, inplace=True)

y_labels = iris_data.iloc[ :, -1 ]              # iris name 라벨
x_data   = iris_data.iloc[ :, :-1]              # iris별 4가지 구분 데이터
print(f'y_labels = {y_labels}')

# On-hot-Encoding 변환
y_labels = np_utils.to_categorical(y_labels, 3)
print(f'y_labels = {y_labels}')

# # 학습 전용과 테스트 전용으로 분리하기
x_train, x_test, y_train, y_test = \
    train_test_split(x_data, y_labels, train_size=0.8)

# (2) 모델 구조 정의 --------------------------------------------
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))  # 입력층
model.add(Dense(3,  activation='softmax'))                 # 출력층

# 모델 구축
model.compile(  loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
print("==*10")
print(model.summary())
print("==*10")

# (3) 학습 실행  ------------------------------------------------
model.fit(x_train,
          y_train,
          batch_size=20,        # 학습 데이터 크기
          epochs=300,           # 반복 횟수  1회 학습에  150번 업데이트 진행
          verbose=1 )

# (5) 모델 평가하기 ----------------------------------------------
score = model.evaluate(x_test, y_test, verbose=1)
print('정답률=', score[1], 'loss=', score[0])

# (6) 모델 저장하기 ----------------------------------------------
# model.save('./Model/iris_model.h5')


