import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import os
import subprocess
import pandas as pd
import numpy as nptx
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LinearRegression

Data_Source = pd.read_csv('Data/TempSamples2/MyFile/Sum.csv')

feature_cols = ['SRCPORTSum','SRCPORTSum','SRCIPSum','DSTIPSum']
X = Data_Source[feature_cols]
y = Data_Source['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
#clf = svm.SVC()
#clf.fit(X_train, y_train)
#y_test = clf.predict(X_test)
#scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
#print(scores)
#linreg = LinearRegression()
#linreg.fit(X_train, y_train)
#y_test = linreg.predict(X_test)
knn = KNeighborsClassifier(n_neighbors=3)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
#k_range = list(range(1, 31))
#param_grid = dict(n_neighbors=k_range)
#grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
#grid.fit(X, y)
#print(grid.best_score_)
#print(grid.best_params_)
#print(grid.best_estimator_)
print(scores)