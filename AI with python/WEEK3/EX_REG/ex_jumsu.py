# =============================================
# Linear Regression 실습 - (1) 데이터 분포 확인
# 공부시간에 따른 점수 예측하기
# =============================================
# 모듈 로딩 ------------------------------------
import matplotlib.pyplot as plt

# 데이터 준비 -----------------------------------
x=[2, 4, 6, 8, 10]                  # 시간
y=[81, 89, 93, 91, 97]              # 성적

# 그래프 그리기 ----------------------------------
plt.plot(x, y, "r^")                # 직선 그래프
plt.xlabel("Hour")
plt.ylabel("Jumsu")
plt.grid()
plt.show()                          # 그래프 화면 출력