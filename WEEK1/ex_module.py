#
import math
import matplotlib.pyplot as mp
from os.path import isfile, exists           # 모듈 안에서 함수 1개 가져오기
import ex_func

ex_func.getMaxMin(*[1,40,2.,6])


print(f"math.pi => {math.pi}")
print(f"math.inf => {math.inf}")
print(f"math.pow(2,3) => {math.pow(2,3)}")
print(f"math.factorial(5) => {math.factorial(5)}")

# 모듈명이 길면 별칭사용
mp.plot([1,2,3,4])
mp.show()

def exists(data):
    print("My Function exists()")

# 함수만 가져왔으면 함수 바로사용
exists("Data")