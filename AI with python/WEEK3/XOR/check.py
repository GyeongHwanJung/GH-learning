import pickle

# 모델 가져오기
with open('xor_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 검사 문제
x_test = [ [1, 1], [0, 0], [0, 1], [1, 0] ]

# 모델 예측
y_predict = model.predict(x_test)
print('y_predict=>', y_predict)



