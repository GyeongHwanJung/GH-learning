import pandas as pd

exam_data={'수학':[90,80,70], '영어':[98,89,95],
           '음악':[85,95,100], '체육':[100,90,90]}

df=pd.DataFrame(exam_data, index=['서준','우현','인아'])
print("df ============================\n", df)

df.loc["길동"]=80
print(f"df =>\n{df}")

df["국어"]=0
print(f"df =>\n{df}")

df["미술"]=[98,92,76,54]
print(f"df=>\n{df}")

df.drop("인아", inplace=True)
print(f"df =>\n{df}")

df.drop("국어", axis=1, inplace=True)
print(f"df =>\n{df}")

df=df.transpose()
print(f"df.transpose() =>\n{df}")

df=df.T
print(f"df=df.T =>\n{df}")

df.sort_values(by='음악', ascending=False)
print(f"sort_values(by='음악', ascending=False)=>\n{df}")

df.sort_values(by='음악')
print(f"sort_values(by='음악')=>\n{df}")

