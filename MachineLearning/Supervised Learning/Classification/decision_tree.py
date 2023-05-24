import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as mt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree

iris = datasets.load_iris()
# print(iris.keys()) # dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])

'''
Bunch 객체 형식으로 제공, keys() 함수로 key값 확인
data속성 : 입력변수(학습에 필요한 특징들, Feature, 독립변수), 꽃받침 길이, 너비, 꽃입 길이, 너비로 예측 예정
target속성 : 출력변수(답안, label, class, 종속변수)
target_name 속성 : class 문자열 배열
feature_namns : 입력 변수의 각 항목별 이름
DESCR : 데이터셋에 대한 설명

'''
irisDF = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(irisDF)

irisDF['label'] = iris.target

X_train, X_test, y_train, y_test = train_test_split(irisDF.loc[:, :'petal width (cm)'], irisDF.label, test_size=0.3, random_state=121)
# print(X_train)
# print(X_test)

dt_clf = DecisionTreeClassifier(random_state=121)
dt_clf.fit(X_train, y_train)

# print(dt_clf.get_depth())
# print(dt_clf.get_n_leaves())

pred = dt_clf.predict(X_test)

print(pred)
# 모델 평가
print(dt_clf.score(X_test, y_test))
print(mt.accuracy_score(y_test, pred))


y_predict = dt_clf.predict(X_test)
plt.figure(figsize=(16, 9))
plot_tree(dt_clf, filled=True, fontsize=14, feature_names=iris.feature_names)
plt.show()