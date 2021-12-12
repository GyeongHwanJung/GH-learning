import pandas as pd

exam_data={'수학':[90,80,70], '영어':[98,89,95],
           '음악':[85,95,100], '체육':[100,90,90]}

df=pd.DataFrame(exam_data, index=['서준','우현','인아'])
print("df ============================\n", df)
print('\n')

label1=df.loc['서준']
position1=df.iloc[0]
print('label1=>\n', label1)
print('\n')
print('position1=>\n', position1)
print('\n')


print(f"df['수학'] =>\n{df.iloc[0,0]}")
print(f"df.loc['서준','수학'] => {df.loc['서준','수학']}\n")

print(f"df.iloc[0,[0,2]] =>\n{df.iloc[0,[0,2]]}")
print(f"df.loc['서준', ['수학', '음악']] =>\n"
      f"{df.loc['서준', ['수학', '음악']]}\n")

print(f"df.iloc[[0,2],[0,2]] =>\n{df.iloc[[0,2],[0,2]]}")
print(f"df.loc[['서준', '인아'], ['수학','음악']] =>\n"
      f"{df.loc[['서준', '인아'], ['수학','음악']]}\n")

print(f"df.iloc[0,1:] =>\n{df.iloc[0,1:]}")
print(f"df.loc[['서준'], ['영어':'체육']] =>\n"
      f"{df.loc[['서준'], ['영어':'체육']]}\n")






#print(f"df[['수학', '음악']] =>\n{df[['수학', '음악']]}")

#print(f"df['수학':'음악'] =>\n{df['수학':'음악']}")