def getSum(*datas):
    value = 0
    for num in datas:
        value += num

#
data=list(range(1,101))
print(f"getSum(2,6,8,10,12,14) => {getSum(*data)}")


def getMaxMin(*datas):
    _max=max(datas)
    _min=min(datas)
    return _max, _min

_max, min=getMaxMin(2,10,87,3,0)
print(f"_max = {_max}, _min = {min}")

_maxmin=getMaxMin(2,10,87,3,0)
print(f"_maxmin={_maxmin}")


def setIDPW(**idpw):
    print(idpw, type(idpw))

setIDPW(id1="a123", id2="kim", id3="go0909")

