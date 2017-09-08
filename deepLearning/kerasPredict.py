import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split

Data_Source = pd.read_csv(
    r'C:\Users\txl78\PycharmProjects\SecurityOperationsCenterRetrieval\Data\processFile\NumberEndFile.csv')
feature_cols = ['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
                'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
                'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
                'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8']
X = Data_Source[feature_cols].values
Y = Data_Source['Result'].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
# create model
model = Sequential()
model.add(Dense(12, input_dim=32, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss="mean_squared_error", optimizer="adam", metrics=['accuracy'])
# Fit the model
model.fit(X_train, Y_train, epochs=100)
Data_Predict = pd.read_csv(
    '../Data/Source/prepredict_Number_response_merged_withHeader.csv')
Data_Predict_Array = Data_Predict.as_matrix(feature_cols)
predictions_Y = model.predict(Data_Predict_Array)
# round predictions
rounded = [round(x[0]) for x in predictions_Y]
predictions_dataframe = pd.DataFrame(np.array(rounded))
# predictions_dataframe=pd.DataFrame(np.array(predictions_Y))
predictions_dataframe.to_csv(
    r"C:\Users\txl78\PycharmProjects\SecurityOperationsCenterRetrieval\Data\Source\prepredict_result.csv")

# Data_Predict_Array=Data_Predict.values
# predictResult=model.predict(Data_Predict_Array)
# print(predictResult.type)
