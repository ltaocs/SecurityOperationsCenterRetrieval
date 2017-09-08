# api = bigml.BigML()
# sapi = bigml.BigML('lintao', '1d424ec03053afba4b8c368bd34ddf189846b06c')
from bigml.api import BigML

# This is not real api key
api = BigML('lintao', '1d4')

source = api.create_source('tempData/TempSamples2/MyFile/TempEndFile.csv')
dataset = api.create_dataset(source)
model = api.create_model(dataset)
prediction = api.create_prediction(model, \
                                   'tempData/TempSamples2/MyFile/TempPredictionEndFile.csv')
api.pprint(prediction)
