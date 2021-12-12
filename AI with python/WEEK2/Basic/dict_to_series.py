# 딕셔너리 데이터 => 시리즈 객체 만들기
import pandas as pd

# 데이터 준비
dict_data={'a':10, 'b':20, 'c':30}

# 시리즈 객체 생성
sObj=pd.Series(dict_data)

# 정보확인
print(f"type(sObj) => {type(sObj)}")
print(f"sObj => {sObj}")
print(f"sObj.index => {sObj.index}")
print(f"sObj.values => {sObj.values}")

# 인덱스 설정 -----------------------------------
sObj.index=["one", "two", "three"]
print(f"sObj =>\n{sObj}")

# 인덱스 일부 변경
sObj.rename(index={"one":1}, inplace=True)
print(f"sObj =>\n{sObj}")
