import pandas as pd


def Read_Data(FilePath):
    # pass in column names for each CSV
    cols_names = ['IndexNo', 'Sequence', 'Operation', 'Source', 'Content', 'Thinking']
    # data = pd.read_csv('Data/TempSamples2/T1_samples1.csv', names=cols_names, header=None)
    data = pd.read_csv(FilePath, names=cols_names, header=None)
    Content_Data = data['Content']

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
    for i in Content_Data:
        i = i.replace('DestPort', 'DSTPORT')
        i = i.replace('SourcePort', 'SRCPORT')
        i = i.replace('SourceIP', 'SRCIP')
        i = i.replace('DesIP', 'DSTIP')

        # One_Feature = pd.Series()
        # DSTPORT
        if (("DSTPORT = '6667'" or "DestPort = '6667'") in i) and DSTPORT <= 8:
            # if(("DSTPORT = '6667'" or "DestPort = '6667'") in i):
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            # One_Feature.loc[LocationIndex] = 6667
            One_Feature.set_value(LocationIndex, 6667)
            DSTPORT = DSTPORT + 1
        if (("DSTPORT = '445'" or "DestPort = '445'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 445
            DSTPORT = DSTPORT + 1
        if (("DSTPORT = '21'" or "DestPort = '21'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 21
            DSTPORT = DSTPORT + 1
        if (("DSTPORT = '22'" or "DestPort = '22'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 22
            DSTPORT = DSTPORT + 1
        if (("DSTPORT = '80'" or "DestPort = '80'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 80
            DSTPORT = DSTPORT + 1
        if (("DSTPORT <> '6667'" or "DestPort <> '6667'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 16667
            DSTPORT = DSTPORT + 1
        if (("DSTPORT <> '445'" or "DestPort <> '445'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 1445
            DSTPORT = DSTPORT + 1
        if (("DSTPORT <> '22'" or "DestPort <> '22'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 122
            DSTPORT = DSTPORT + 1
        if (("DSTPORT <> '21'" or "DestPort <> '21'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 121
            DSTPORT = DSTPORT + 1
        if (("DSTPORT <> '80'" or "DestPort <> '80'") in i) and DSTPORT <= 8:
            LocationIndex = 'DSTPORT' + str(DSTPORT)
            One_Feature.loc[LocationIndex] = 180
            DSTPORT = DSTPORT + 1
        # SRCPORT
        if (("SRCPORT = '6667'" or "SourcePort = '6667'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 6667
            SRCPORT = SRCPORT + 1
        if (("SRCPORT = '445'" or "SourcePort = '445'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 445
            SRCPORT = SRCPORT + 1
        if (("SRCPORT = '80'" or "SourcePort = '80'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 80
            SRCPORT = SRCPORT + 1
        if (("SRCPORT = '21'" or "SourcePort = '21'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 21
            SRCPORT = SRCPORT + 1
        if (("SRCPORT = '22'" or "SourcePort = '22'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 22
            SRCPORT = SRCPORT + 1
        if (("SRCPORT <> '6667'" or "SourcePort <> '6667'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 16667
            SRCPORT = SRCPORT + 1
        if (("SRCPORT <> '445'" or "SourcePort <> '445'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 1445
            SRCPORT = SRCPORT + 1
        if (("SRCPORT <> '22'" or "SourcePort <> '22'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 122
            SRCPORT = SRCPORT + 1
        if (("SRCPORT <> '21'" or "SourcePort <> '21'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 121
            SRCPORT = SRCPORT + 1
        if (("SRCPORT <> '80'" or "SourcePort <> '80'") in i) and SRCPORT <= 8:
            LocationIndex = 'SRCPORT' + str(SRCPORT)
            One_Feature.loc[LocationIndex] = 180
            SRCPORT = SRCPORT + 1

        # SRCIP
        if (("SRCIP > '172" or "SourceIP > '172" or "SRCIP = '172'") in i) and SRCIP <= 8:
            LocationIndex = 'SRCIP' + str(SRCIP)
            One_Feature.loc[LocationIndex] = 172
            SRCIP = SRCIP + 1
        if (("SRCIP > '10" or "SourceIP > '10" or "SRCIP = '172'") in i) and SRCIP <= 8:
            LocationIndex = 'SRCIP' + str(SRCIP)
            One_Feature.loc[LocationIndex] = 10
            SRCIP = SRCIP + 1
        # DSTIP
        if (("DSTIP > '172" or "DSTIP > '172" or "DSTIP = '172'") in i) and DSTIP <= 8:
            LocationIndex = 'DSTIP' + str(DSTIP)
            One_Feature.loc[LocationIndex] = 172
            DSTIP = DSTIP + 1

        if (("DSTIP > '10" or "DSTIP > '10" or "DSTIP = '10'") in i) and DSTIP <= 8:
            LocationIndex = 'DSTIP' + str(DSTIP)
            One_Feature.loc[LocationIndex] = 10
            DSTIP = DSTIP + 1

    return One_Feature


Classification_Data = pd.DataFrame(
    columns=['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
             'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
             'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
             'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8'])

Lable_Result_File = pd.read_csv("Data/TempSamples2/MyFile/lable results.csv")
for i in range(0, 304):
    Process_Data_One = Read_Data('Data/TempSamples2/' + Lable_Result_File['Trace1'][i])
    Process_Data_Two = Read_Data('Data/TempSamples2/' + Lable_Result_File['Trace2'][i])
    Result_Series = pd.Series(Process_Data_One == Process_Data_Two)
    Classification_Data = Classification_Data.append(Result_Series, ignore_index=True)
Classification_Data['Result'] = Lable_Result_File['Tao']
Classification_Data.to_csv('Data/TempSamples2/MyFile/EndFile.csv')
