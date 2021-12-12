# 모듈 로딩 -------------------------------------
import pandas as pd
from matplotlib import cm
from sklearn import svm, metrics
import matplotlib.pyplot as plt
import numpy as np

# 데이버 변수 선언 --------------------------------
# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# (1) 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류
xor_df = pd.DataFrame(xor_input)
print("---- xor_df -----\n", xor_df )
xor_data = xor_df.iloc[:, 0:2]           #iloc[행, 열 index]
xor_label = xor_df.iloc[:,2]

print("---- xor_data -----\n", xor_data )
print("---- xor_label -----\n", xor_label )

# (2) 데이터 학습과 예측 -----------------------------------
clf = svm.SVC()
clf.fit(xor_data, xor_label)  # 학습
print('clf.class_weight_=>', clf.class_weight_ )
print('clf.support_vectors_=>', clf.support_vectors_)

# (3) 데이터 예측 -----------------------------------
pre = clf.predict(xor_data)   # 예측

# 정답 추출
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)

# (4) 새로운 데이터로 값 예측하기
print("TEST =", ac_score)

# # 그래프 시각화 -----------------------------------------------------
# (2) 그래프 활용 데이터 확인
ax = plt.axes(projection='3d')  # 3차원 그래프
ax.set_xlabel('P')
ax.set_ylabel('Q')
ax.set_zlabel('P xor Q')


# # (4) 면 그래프 ------------------------------------------------------
X1=np.arange(0, 1, 0.1)                      # 공부시간
X2=np.arange(0, 1, 0.1)                      # 보충횟수
X1, X2 = np.meshgrid(X1, X2)                 # 좌표변환
Y = (clf.class_weight_[0]*X1) + (clf.class_weight_[1]*X2)+clf.intercept_        # 점수
#
ax.plot_surface(X1, X2, Y,
                rstride=4, cstride=4, alpha=0.4, cmap=cm.rainbow)

#fig, ax = plt.subplots()
ax.scatter(0, 0, 0, color="g")
ax.scatter(0, 1, 1, color="r")
ax.scatter(1, 0, 1, color="r")
ax.scatter(1, 1, 0, color="g")
#ax.set_xlim([-0.2, 1.4])
#ax.set_ylim([-0.1, 1.1])
# m = -1
# plt.plot()
plt.show()
