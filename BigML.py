import bigml.api
from bigml import api
from bigml.api import BigML

# api = bigml.BigML()
# sapi = bigml.BigML('lintao', '1d424ec03053afba4b8c368bd34ddf189846b06c')
from bigml.api import BigML
api = BigML('lintao', '1d424ec03053afba4b8c368bd34ddf189846b06c')

source = api.create_source('Data/TempSamples2/MyFile/TempEndFile.csv')
dataset = api.create_dataset(source)
model = api.create_model(dataset)
prediction = api.create_prediction(model, \
                                   'Data/TempSamples2/MyFile/TempPredictionEndFile.csv')
api.pprint(prediction)