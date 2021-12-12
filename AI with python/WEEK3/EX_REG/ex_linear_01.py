import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 데이터 -----------------------------
# x=np.array([6,8, 10, 15, 18])
# y=np.array([7,9,13, 17.5, 19.3])

x=[6,8, 10, 15, 18]
y=[7,9,13, 17.5, 19.3]

# 함수 선언 --------------------------
# /x=x.reshape(-1,1)   # 2차원으로 변경

# 모델 객체 생성 ------------------------
model= LinearRegression()
model.fit(x, y)

plt.figure()
plt.plot(x, y, 'ro')
plt.plot(x, model.predict(x), 'k--')
print("w =>", model.coef_, "b => ", model.intercept_)
print("model.score(x,y)=>", model.score(x,y))
plt.plot(x, x*model.coef_+model.intercept_, 'r--')
plt.title('Pizza Price(inch)')
plt.xlabel('Inches')
plt.ylabel('Price')
plt.axis([0, 25, 0, 25])
plt.grid()
plt.show()

