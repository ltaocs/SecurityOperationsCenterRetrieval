import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pass in column names for each CSV
cols_names = ['IndexNo', 'Sequence', 'Operation', 'Source', 'Content', 'Thinking']
# data = pd.read_csv('Data/TempSamples2/T1_samples1.csv', names=cols_names, header=None)
data = pd.read_csv('Data/TempSamples2/T4_samples1.csv', names=cols_names, header=None)
Content_Data = data['Content']
# print(Content_Data)
# define Classification Data

DSTPORT = 1
SRCPORT = 1
SRCIP = 1
DSTIP = 1

One_Feature = pd.Series(
    index=['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
           'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
           'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
           'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8'])
i="SRCPORT = '80'"
if (("SRCPORT = '445'" or "SourcePort = '6667'") in i) and SRCPORT <= 8:
    LocationIndex = 'SRCPORT' + str(SRCPORT)
    One_Feature.loc[LocationIndex] = 6667
    SRCPORT = SRCPORT + 1
print(One_Feature)
