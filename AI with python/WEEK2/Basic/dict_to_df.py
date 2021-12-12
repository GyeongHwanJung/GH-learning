# 딕셔너리 테이터 => 데이터 프레임 생성
import pandas as pd

# 데이터 준비 ---------------------------
dict_data={"name":["HKG","LEE","PARK"],
           "age":[15,21,5],
           "gender":["F","M","M"]
           }

df=pd.DataFrame(dict_data)

print(f"type(df) => {type(df)}")
print(f"df =>\n{df}")
print(f"df.index => {df.index}")
print(f"df.columns => {df.columns}")
print(f"df.values =>\n{df.values}")

df.index=[10,11,12]
print()