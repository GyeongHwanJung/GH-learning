# 리스트 데이터 => 데이터 프레임 생성
import pandas as pd

list_data=[ [11,12,13], [21,22,23], [31,32,33] ]

df=pd.DataFrame(list_data)
df2=pd.DataFrame(list_data,
                 index=['one','two','three'],
                 columns=['A','B','C'])


print(f"type(df) => {type(df)}")
print(f"df =>\n{df}")
print(f"df.index => {df.index}")
print(f"df.columns => {df.columns}")
print(f"df.values =>\n{df.values}")

print(f"type(df2) => {type(df2)}")
print(f"df2 =>\n{df2}")
print(f"df2.index => {df2.index}")
print(f"df2.columns => {df2.columns}")
print(f"df2.values =>\n{df2.values}")
