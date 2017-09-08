import pandas as pd
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

Data_Source = pd.read_csv('tempData/TempSamples2/MyFile/Sum.csv')

feature_cols = ['SRCPORTSum', 'SRCPORTSum', 'SRCIPSum', 'DSTIPSum']
X = Data_Source[feature_cols]
y = Data_Source['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
clf = svm.SVC()
clf.fit(X_train, y_train)
predict_y = clf.predict(X_test)
scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
print(scores)

# linreg = LinearRegression()
# linreg.fit(X_train, y_train)
# y_test = linreg.predict(X_test)
# knn = KNeighborsClassifier(n_neighbors=3)
# scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')

# print(scores)
