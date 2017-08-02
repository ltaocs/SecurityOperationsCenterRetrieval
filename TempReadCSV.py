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
i="SRCPORT = '6667'"
if (i.find("DSTPORT = '6667'" or "DestPort = '6667'")) and DSTPORT <= 8:
    # if(("DSTPORT = '6667'" or "DestPort = '6667'") in i):
    LocationIndex = 'DSTPORT' + str(DSTPORT)
    # One_Feature.loc[LocationIndex] = 6667
    One_Feature.set_value(LocationIndex, 6667)
    DSTPORT = DSTPORT + 1
if (i.find("DSTPORT = '445'" or "DestPort = '445'")) and DSTPORT <= 8:
    LocationIndex = 'DSTPORT' + str(DSTPORT)
    One_Feature.loc[LocationIndex] = 445
    DSTPORT = DSTPORT + 1
if ((i.find("DSTPORT \<\> '6667'" or "DestPort \<\> '6667'")) and DSTPORT <= 8):
    LocationIndex = 'DSTPORT' + str(DSTPORT)
    One_Feature.loc[LocationIndex] = 16667
    DSTPORT = DSTPORT + 1
if ((i.find("DSTPORT <> '445'" or "DestPort <> '445'")) and DSTPORT <= 8):
    LocationIndex = 'DSTPORT' + str(DSTPORT)
    One_Feature.loc[LocationIndex] = 1445
    DSTPORT = DSTPORT + 1
# SRCPORT
if (i.find("SRCPORT = '6667'" or "SRCIP = '6667'")) and SRCPORT <= 8:
    LocationIndex = 'SRCPORT' + str(SRCPORT)
    One_Feature.loc[LocationIndex] = 6667
    SRCPORT = SRCPORT + 1
if (i.find("SRCPORT = '445'" or "SRCIP = '445'")) and SRCPORT <= 8:
    LocationIndex = 'SRCPORT' + str(SRCPORT)
    One_Feature.loc[LocationIndex] = 445
    SRCPORT = SRCPORT + 1
if ((i.find("SRCPORT \<\> '6667'" or "SRCIP \<\> '6667'")) and SRCPORT <= 8):
    LocationIndex = 'SRCPORT' + str(SRCPORT)
    One_Feature.loc[LocationIndex] = 16667
    SRCPORT = SRCPORT + 1
if ((i.find("SRCPORT \<\> '445'" or "SRCIP \<\> '445'")) and SRCPORT <= 8):
    LocationIndex = 'SRCPORT' + str(SRCPORT)
    One_Feature.loc[LocationIndex] = 1445
    SRCPORT = SRCPORT + 1
# SRCIP
if ((i.find("SRCIP > '172" or "SourceIP > '172")) and SRCIP <= 8):
    LocationIndex = 'SRCIP' + str(SRCIP)
    One_Feature.loc[LocationIndex] = 172
    SRCIP = SRCIP + 1
if ((i.find("SRCIP >= '10.32.5.50'" or "SourceIP > '10")) and SRCIP <= 8):
    LocationIndex = 'SRCIP' + str(SRCIP)
    One_Feature.loc[LocationIndex] = i
    SRCIP = SRCIP + 1
# DSTIP
if ((i.find("DSTIP > '172." or "DSTIP > '172.")) and DSTIP <= 8):
    LocationIndex = 'DSTIP' + str(DSTIP)
    One_Feature.loc[LocationIndex] = 172
    DSTIP = DSTIP + 1

if ((i.find("DSTIP > '10" or "DSTIP > '10")) and DSTIP <= 8):
    LocationIndex = 'DSTIP' + str(DSTIP)
    One_Feature.loc[LocationIndex] = 10
    DSTIP = DSTIP + 1
print(One_Feature)
