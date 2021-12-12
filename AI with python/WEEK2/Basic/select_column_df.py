import pandas as pd

exam_data={'수학':[90,80,70], '영어':[98,89,95],
           '음악':[85,95,100], '체육':[100,90,90]}

df=pd.DataFrame(exam_data, index=['서준','우현','인아'])
print("df ============================\n", df)
print('\n')

label1=df.loc['서준']
position1=df.iloc[0]
print('label1=>', label1)
print('\n')
print('position1=>', position1)
print('\n')


print(f"df['수학'] =>\n{df['수학']}")
print(f"df.수학 =>\n{df.수학}\n")

print(f"df[['수학', '음악']] =>\n{df[['수학', '음악']]}")

print(f"df['수학':'음악'] =>\n{df['수학':'음악']}")