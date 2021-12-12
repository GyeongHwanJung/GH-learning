#=============================================
# Linear Regression 실습 => (4) 최적화
#           경사하강법 활용 -> W, b를 찾기위한 방법
# =============================================
# 모듈 로딩 ------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비 -----------------------------------
x=[2, 4, 6, 8, 10]         # 시간 데이터
y=[81, 89, 93, 91, 97]     # 점수 데이터

# 연산 수행 위해서 데이터 변형
x_data = np.array(x)
y_data = np.array(y)

#print(f"x_data+y_data => {x_data+y_data}")

# 그래프 그리기 -----------------------------------
plt.figure(figsize=(8,5))
plt.scatter(x, y)               # 산점도
plt.show()

# # 전역변수 선언 -----------------------------------
w = 0               # 임의의 기울기(w)
b = 0               # 절편 초기화
lr = 0.03           # 학습률 초기화
epochs = 500        # 반복 횟수

# # 기능 구현 ======================================
print(f"x_data =>{x_data}")
print(f"y_data =>{y_data}")

# # 평균제곱오차 계산 함수 --------------------------------
# 오차 계산 MSE 함수
def mse(predict_result,y):
   return ((predict_result - y) ** 2).mean()

# MSE 함수를 각 y값에 대입하여 최종 값을 구하는 함수
def mse_val(predict_result,y):
   return mse( np.array(predict_result),np.array(y) )

def getMSE(predict_result, y):
   return mse_val(predict_result, y)

# # 경사하강법 최적화 ---------------------------------
# a 즉, w와 b 찾기
# range(11)  => 0,1,2,3,4,5,6,7,8,9,10 0~10
for i in range(epochs):         # epoch 수 만큼 반복
    y_pre = w * x_data + b      # y = ax+b
    error = y_data - y_pre      # 오차 계산
    #print(f"{i} y_pre =>{y_pre}, error => {error}")

    # a,b 미분값 계산
    w_diff = -(2/len(x_data)) * sum(x_data * (error))   # 오차함수를 a로 미분한 값
    b_diff = -(2/len(x_data)) * sum(error)              # 오차함수를 b로 미분한 값
    w = w - lr * w_diff                                 # 학습률을 곱해 기존의 a값을 업데이트
    b = b - lr * b_diff                                 # 학습률을 곱해 기존의 b값을 업데이트
    if i % 100 == 0:                                   # 100번 반복될 때마다 현재의 a값, b값을 출력
        print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, w, b))
        print(f"error=>{error}")

print(f"MSE => { getMSE(y_pre, y_data)}")

# # 앞서 구한 기울기와 절편을 이용해 그래프
# y_pred = a * x_data + b
# print(f"y_pred=>{y_pred}")
# print(f"x_data=>{x_data}")
# plt.scatter(x, y)
# plt.plot(x_data, y_pred)
# plt.show()

