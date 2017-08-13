import pandas as pd

# pass in column names for each CSV
cols_names = ['IndexNo', 'Sequence', 'Operation', 'Source', 'Content', 'Thinking']
# data = pd.read_csv('Data/TempSamples2/T1_samples1.csv', names=cols_names, header=None)
data = pd.read_csv('Data/TempSamples2/T1_samples2.csv', names=cols_names, header=None)
# Content_Data = data['Content']
import tkinter
