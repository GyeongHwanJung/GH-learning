# ==============================================
# Linear Regression 실습 - (2) 직선(가설) 구하기
#   y=Wx+b    => W, b 구하기 : 최소제곱법
# ==============================================
# 모듈 로딩 -------------------------------------
import matplotlib.pyplot as plt    # 그래프 모듈
import numpy as np                 # 수치 계산 모듈

# 데이터 준비 -----------------------------------
x=[2, 4, 6, 8, 10]
y=[81, 89, 93, 91, 97]

# 전역변수 선언 -------------------------------
# 최소제곱법 관련 변수들
mx = np.mean(x)
my = np.mean(y)
print("x 평균값:", mx, " y 평균값:", my)

# 기울기 공식의 분모
# (x평균-x1)2 +…+ (x평균-xn)2
divisor = sum( [ (mx - i)**2 for i in x  ]  )

# 함수 선언 -------------------------------------
# 기울기 공식의 분자
# (x1-x평균)*(y1-y평균) +…+ (XN-x평균)*(yN-y평균)
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d

# 기울기 공식의 분자
dividend = top(x, mx, y, my)
print("분모:", divisor, " 분자:", dividend)

# 기울기와 절편 구하기-------------------------
w = dividend / divisor
b = my - (mx*w)                 # b=y-ax

# 출력으로 확인
print("기울기 w =", w, "y 절편 b =", b)
print(f"가설(일차함수) y ={w}x+{b}")

# 가설 공식에 x 데이터 적용 후 예측 y2 값 추출
y2=[ (w*i)+b for i in x ]

# 그래프 그리기 ----------------------------------
plt.plot(x, y, "r^")          # 정답 데이터
plt.plot(x, y2, "b--")        # 가설 직선
plt.plot(x, y2, "b^")         # 가설의 정답 데이터
plt.xlabel("Hour")
plt.ylabel("Jumsu")
plt.grid()
plt.show()


# 일차함수의 a(기울기),b(절편) 반환 함수 ---------------------------
# def getLineValue(x, y):
#     mx = np.mean(x)
#     my = np.mean(y)
#     #print("x의 평균값:", mx, " y의 평균값:", my)
#
#     # 기울기 공식의 분모
#     divisor = sum([(mx - i) ** 2 for i in x])
#     dividend = top(x, mx, y, my)
#     #print("분모:", divisor, " 분자:", dividend)
#
#     # 기울기와 y 절편 구하기-------------------------
#     a = dividend / divisor
#     b = my - (mx * a)
#
#     # 출력으로 확인
#     #print("기울기 a =", a, " y 절편 b =", b)
#
#     return a, b     # 튜플타입  (a,b)   a,b




