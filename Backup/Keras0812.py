import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
# import the necessary packages
from sklearn.cross_validation import train_test_split

Data_Source = pd.read_csv('Data/TempSamples2/MyFile/TempNumberEndFile.csv')
feature_cols = ['DSTPORT1', 'DSTPORT2']
X = Data_Source[feature_cols]
Y = Data_Source['Result']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
# Define the model
model = Sequential()
model.add(Dense(5, input_dim=2, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')

newX=np.array(X_train)
newY=np.array(Y_train)


# Train the model
model.fit(
    newX,
    newY,
    epochs=50,
    shuffle=True,
    verbose=2
)