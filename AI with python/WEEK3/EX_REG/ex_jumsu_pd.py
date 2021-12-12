# =============================================
# Linear Regression 실습 - 데이터 분포 확인
# =============================================
# 모듈 로딩 ------------------------------------
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 준비 -----------------------------------
df=pd.read_excel("../Data/jumsu.xlsx")
print(f"df => \n{df}")
x=[2, 4, 6, 8, 10]                      # 시간
y=[81, 89, 93, 91, 97]                  # 성적

# 그래프 그리기 ----------------------------------
plt.plot(x, y, "r^")                    # 정답 데이터
plt.xlabel("Hour")
plt.ylabel("Jumsu")
plt.grid()
plt.show()
