from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.utils import all_estimators

# estimators=all_estimators(type_filter='classifier0')
# all_regs=[]
# for name, ClassifierClass in estimators:
#     try:
#         all_regs.append(name)
#     except Exception:
#         pass
#
# for model in all_regs: print(model)

iris=load_iris()

X1=iris.data
Y1=iris.data
X1=X1[:, :2]

estimators = all_estimators(type_filter='classifier')
all_esti=[]
for name,  ClassifierClass in estimators:
    try:
        clf=ClassifierClass()
        clf.fit(X1, Y1)

        Y1_pred=clf.predict(X1)
        ac_score=accuracy_score(Y1, Y1_pred)

        all_esti.append([name, round(ac_score, 2)])
    except Exception as e:
        pass

all_esti.sort(key=lambda X:X[1], reverse=True)
for item in all_esti:
    print(item)