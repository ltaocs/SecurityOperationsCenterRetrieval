# Accuracy 73.69% (+/- 7.51%)
# This module use sum.csv
import os

import numpy
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import StratifiedKFold

# fix random seed for reproducibility
seed = 2
numpy.random.seed(seed)
my_path = os.path.abspath(os.path.dirname(__file__))
FileSum = os.path.join(my_path, '../tempData/TempSamples2/MyFile/Sum.csv')
Data_Source = pd.read_csv(FileSum)
feature_cols = ['DSTPORTSum', 'SRCPORTSum', 'SRCIPSum', 'DSTIPSum']
X = Data_Source[feature_cols].values
Y = Data_Source['Result'].values

# define 10-fold cross validation test harness
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
cvscores = []
for train, test in kfold.split(X, Y):
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=4, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X[train], Y[train], epochs=150, batch_size=10, verbose=0)
    # evaluate the model
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
