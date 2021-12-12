import numpy as np
import matplotlib.pyplot as plt

# 데이터 -----------------------------
x=np.array([6,8, 10, 15, 18])
y=np.array([7,9,13, 17.5, 19.3])
x=[6,8, 10, 15, 18]
y=[7,9,13, 17.5, 19.3]

# 함수 선언 --------------------------
def drwa_linear(data):
    return data*2

def drwa_linear2(data):
    return data*1.2

plt.figure()
plt.plot(x, y, 'ro')
#plt.plot(x, drwa_linear(x), 'k--')
#plt.plot(x, drwa_linear2(x), 'g--')
plt.title('Pizza Price(inch)')
plt.xlabel('Inches')
plt.ylabel('Price')
plt.axis([0, 25, 0, 25])
plt.grid()
plt.show()

