# ------------------------------------------------------
# 리스트 데이터
# -----------------------------------------------
# 모듈 로딩
import pandas as pd

# 데이터 준비
list_data=['2021-02-02', 3.15, False, 100]

# 시리즈 객체 생성
sObj=pd.Series(list_data)
sObj2=pd.Series(list_data,
                index=['date','avg','bool','num'])

# 데이터 정보 확인
print(f"type(sObj) => {type(sObj)}")
print(f"sObj => {sObj}")
print(f"sObj.index => {sObj.index}")
print(f"sObj.values => {sObj.values}")

print(f"\ntype(sObj2) => {type(sObj2)}")
print(f"sObj2 => {sObj2}")
print(f"sObj2.index => {sObj2.index}")
print(f"sObj2.values => {sObj2.values}")