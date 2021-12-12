#
def setIDPW(**idpw):
    print(idpw, type(idpw))

setIDPW(id1="a123", id2="kim", id3="go0909")

tdata={'name':'kkk', 'age':12}
setIDPW(**tdata)


#
data=[1,3,5,7,9]

data2=map(lambda x : x+x, data)
print(f"data2 => {data2}")

data=['1','2','3','4']
for idx in range(len(data)):
    data[idx]=int(data[idx])
print(data)

data2=['1','2','3','4']
print(f'data2=>{data2}')
data2=list(map(int, data2))
print(f'data2=>{data2}')