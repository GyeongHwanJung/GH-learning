# ====================================================
# Linear Regression 실습 - Multi-Linear Regression
# ====================================================
# 모듈 로딩 ============================================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm                # colormap 클래스
from EX_REG.ex_jumsu_mse import getMSE     # 함수만 포함

# 데이터 확인 ===========================================
# (1) 데이터 준비
# [공부시간, 보충횟수, 점수]
data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x1 = [i[0] for i in data]       # 공부시간 데이터
x2 = [i[1] for i in data]       # 보충횟수 데이터
y = [i[2] for i in data]        # 성적

# (2) 그래프 활용 데이터 확인
ax = plt.axes(projection='3d')  # 3차원 그래프
ax.set_xlabel('study_hours')
ax.set_ylabel('private_class')
ax.set_zlabel('Score')
ax.scatter(x1, x2, y, c="red", s=30)
#plt.show()

# 학습 모델링 ===========================================
# (1) ML용 데이터 변환
x1_data = np.array(x1)
x2_data = np.array(x2)
y_data  = np.array(y)

# (2) 러닝 관련 변수 선언
# y=a1x1 + a2x2 + b
a1 = 0              # 기울기
a2 = 0              # 기울기
b  = 0              # 절편
lr = 0.02           # 학습률
epochs = 2000       # 반복 횟수

# # (3) 경사 하강법 학습 --------------------------------
for i in range(epochs):
    y_pred = a1 * x1_data + a2 * x2_data + b    # 가설에 의한 예측값
    error = y_data - y_pred                     # 오차

    # 오차함수를 미분한 값 계산
    a1_diff = -(2/len(x1_data)) * sum(x1_data * (error)) # 오차함수를 a1로 미분한 값
    a2_diff = -(2/len(x2_data)) * sum(x2_data * (error)) # 오차함수를 a2로 미분한 값
    b_new = -(2/len(x1_data)) * sum(y_data - y_pred)     # 오차함수를 b로 미분한 값

    # a1, a2, b 새롭게 업데이트
    a1 = a1 - lr * a1_diff      # 학습률을 곱해 기존의 a1값을 업데이트
    a2 = a2 - lr * a2_diff      # 학습률을 곱해 기존의 a2값을 업데이트
    b = b - lr * b_new          # 학습률을 곱해 기존의 b값을 업데이트

    # a1, a2, b 업데이트 과정 출력
    # if i % 100 == 0:            # 100번 반복될 때마다 현재의 a1, a2, b값을 출력
    #     print("epoch=%.f, 기울기1=%.04f, 기울기2=%.04f, 절편=%.04f"
    #            % (i, a1, a2, b))
    mse=getMSE(y_pred, y_data)
    print(f"mse => {mse}")
    if mse <=0.05:
        print("epoch=%.f, 기울기1=%.04f, 기울기2=%.04f, 절편=%.04f" % (i, a1, a2, b))
        break

# # (4) 면 그래프 ------------------------------------------------------
X1=np.arange(2, 8, 0.1)         # 공부시간
X2=np.arange(0, 4, 0.1)         # 보충횟수
X1, X2 = np.meshgrid(X1, X2)    # 좌표변환
Y = (a1 * X1) + (a2 * X2) + b   # 점수

ax.plot_surface(X1, X2, Y,
                rstride=4, cstride=4, alpha=0.4, cmap=cm.rainbow)
plt.show()


