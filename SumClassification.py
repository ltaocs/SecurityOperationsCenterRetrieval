import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

Data_Source = pd.read_csv('tempData/TempSamples2/MyFile/Sum.csv')

feature_cols = ['SRCPORTSum', 'SRCPORTSum', 'SRCIPSum', 'DSTIPSum']
X = Data_Source[feature_cols]
y = Data_Source['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# clf = svm.SVC()
# clf.fit(X_train, y_train)
# y_test = clf.predict(X_test)
# scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
# print(scores)
# linreg = LinearRegression()
# linreg.fit(X_train, y_train)
# y_test = linreg.predict(X_test)
knn = KNeighborsClassifier(n_neighbors=3)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
# k_range = list(range(1, 31))
# param_grid = dict(n_neighbors=k_range)
# grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
# grid.fit(X, y)
# print(grid.best_score_)
# print(grid.best_params_)
# print(grid.best_estimator_)
print(scores)
