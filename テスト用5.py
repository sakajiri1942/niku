from sklearn import datasets
from sklearn.model_selection import train_test_split

mozi = datasets.load_digits()


X = mozi.data
y = mozi.target

(X_train, X_test, y_train, y_test) = train_test_split(X, y, )

from sklearn import svm
clf = svm.SVC(gamma=0.001)

clf.fit(X_train, y_train)

from sklearn import metrics

accuracy = clf.score(X_test, y_test)
print(f"正解率{accuracy}")

predicted = clf.predict(X_test)


print(metrics.classification_report(y_test, predicted))