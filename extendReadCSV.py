import re

import pandas as pd


def Read_Data(FilePath):
    # pass in column names for each CSV
    cols_names = ['IndexNo', 'Sequence', 'Operation', 'Source', 'Content', 'Thinking']
    data = pd.read_csv(FilePath, names=cols_names, header=None)
    Content_Data = data['Content']

    # define Classification tempData

    DSTPORT = 1
    SRCPORT = 1
    SRCIP = 1
    DSTIP = 1

    One_Feature = pd.Series(
        index=['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
               'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
               'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
               'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8'])
    for i in Content_Data:
        i = i.replace('DestPort', 'DSTPORT')
        i = i.replace('SourcePort', 'SRCPORT')
        i = i.replace('SourceIP', 'SRCIP')
        i = i.replace('DesIP', 'DSTIP')
        # Extract the number of DSTPORT,SRCPORT,SRCIP
        xDSTPORT = re.findall('DSTPORT = \'([0-9]+)', i)
        xNotDSTPORT = re.findall('DSTPORT <> \'([0-9]+)', i)
        xSRCPORT = re.findall('SRCPORT = \'([0-9]+)', i)
        xNotSRCPORT = re.findall('SRCPORT <> \'([0-9]+)', i)
        xSRCIP = re.findall('SRCIP [=<] \'([0-9]+)', i)
        xDSTIP = re.findall('SRCIP [=<] \'([0-9]+)', i)

        # One_Feature = pd.Series()
        # DSTPORT
        for xElement in xDSTPORT:
            if DSTPORT <= 8:
                LocationIndex = 'DSTPORT' + str(DSTPORT)
                One_Feature.set_value(LocationIndex, xElement)
                DSTPORT = DSTPORT + 1
        for xElement in xNotDSTPORT:
            if DSTPORT <= 8:
                LocationIndex = 'DSTPORT' + str(DSTPORT)
                xElement = 1 + int(xElement)
                One_Feature.set_value(LocationIndex, xElement)
                DSTPORT = DSTPORT + 1

        # SRCPORT
        for xElement in xSRCPORT:
            if SRCPORT <= 8:
                LocationIndex = 'SRCPORT' + str(SRCPORT)
                One_Feature.set_value(LocationIndex, xElement)
                SRCPORT = SRCPORT + 1
        for xElement in xNotSRCPORT:
            if SRCPORT <= 8:
                LocationIndex = 'SRCPORT' + str(SRCPORT)
                xElement = 1 + int(xElement)
                One_Feature.set_value(LocationIndex, xElement)
                SRCPORT = SRCPORT + 1

        # SRCIP
        for xElement in xSRCIP:
            if SRCIP <= 8:
                LocationIndex = 'SRCIP' + str(SRCIP)
                One_Feature.set_value(LocationIndex, xElement)
                SRCIP = SRCIP + 1
        # DSTIP
        for xElement in xDSTIP:
            if DSTIP <= 8:
                LocationIndex = 'DSTIP' + str(DSTIP)
                One_Feature.set_value(LocationIndex, xElement)
                DSTIP = DSTIP + 1

    return One_Feature


Classification_Data = pd.DataFrame(
    columns=['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
             'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
             'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
             'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8'])

Lable_Result_File = pd.read_csv("tempData/TempSamples2/MyFile/tempextendLabelResults.csv")
CSVLength = len(Lable_Result_File.index)
for i in range(0, CSVLength):
    Process_Data_One = Read_Data('tempData/TempSamples2/' + Lable_Result_File['Trace1'][i])
    Process_Data_Two = Read_Data('tempData/TempSamples2/' + Lable_Result_File['Trace2'][i])
    Result_Series = pd.Series(Process_Data_One == Process_Data_Two)
    Classification_Data = Classification_Data.append(Result_Series, ignore_index=True)
Classification_Data['Result'] = Lable_Result_File['Tao']
Classification_Data.to_csv('tempData/TempSamples2/MyFile/extendEndFile.csv')
