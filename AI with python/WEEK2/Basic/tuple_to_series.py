# ------------------------------------------------------
# 튜플 데이터
# -----------------------------------------------
# 모듈 로딩
import pandas as pd

# 데이터 준비
tuple_data=['2021-02-02', 3.15, False, 100]

# 튜플 객체 생성
sObj=pd.Series(tuple_data)

# 데이터 정보 확인
print(f"type(sObj) => {type(sObj)}")
print(f"sObj => {sObj}")
print(f"sObj.index => {sObj.index}")
print(f"sObj.values => {sObj.values}")