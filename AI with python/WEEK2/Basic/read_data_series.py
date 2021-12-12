# 딕셔너리 데이터 => 시리즈 객체 만들기
# 요소(원소) 데이터 읽기
import pandas as pd

# 데이터 준비
dict_data={'a':10, 'b':20, 'c':30, 'd':40, 'e':50}

# 시리즈 객체 생성
sObj=pd.Series(dict_data)

# 정보확인
print(f"type(sObj) => {type(sObj)}")
print(f"sObj => {sObj}")
print(f"sObj.index => {sObj.index}")
print(f"sObj.values => {sObj.values}")

# 인덱스 설정 -----------------------------------
# 인덱스 번호 또는 이름
print("\n ===== 요소 값 읽기 ===== ")
print(f"sObj[0] => {sObj[0]}")
print(f"sObj['a'] => {sObj['a']}")

print("\n == 요소 값 여러개 읽기 == ")
print(f"sObj[[0, 2]] => \n{sObj[[0, 2]]}")
print(f"sObj[['a', 'c']] => \n{sObj[['a', 'c']]}")

# 번호 : 끝번호 데이터 미포함
# 이름 : 끝이름 데이터 포함
print("\n == 연속된 요소 값 읽기 == ")
print(f"sObj[ 1:4 ] => \n{sObj[ 1:4 ]}")
print(f"sObj[ 'b':'e' ] => \n{sObj[ 'b':'e' ]}")