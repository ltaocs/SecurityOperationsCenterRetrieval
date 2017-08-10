import pandas as pd

# pass in column names for each CSV
cols_names = ['IndexNo', 'Sequence', 'Operation', 'Source', 'Content', 'Thinking']
data = pd.read_csv('Data/TempSamples2/T1_samples1.csv', names=cols_names, header=None)
Content_Data = data['Content']

# define Classification Data
Classification_Data = pd.DataFrame(
    columns=['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8', 'SRCPORT1',
             'SRCPORT1', 'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT17',
             'SRCPORT8', 'SRCIP1', 'SRCIP1', 'SRCIP1', 'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6',
             'SRCIP7', 'SRCIP8', 'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8'])
DSTPORT = 0
for i in Content_Data:
    if (i.find("DSTPORT = '6667'")) and DSTPORT < 8:
        # Classification_Data.set_value(index=1,col=1,value=6667,takeable=False)
        Classification_Data.set_value(0, 0, 6667)
print(Classification_Data)
