import pandas as pd
import numpy as np 
import csv

#take file ids of trips with 0s for camera confidence and store in a new .csv
df = pd.read_csv('H:\CameraProbabilities\Cam&Lights.csv', usecols = ['file_id', 'left_marker_%perfect']) 

for col in df: 
    column = df.loc[:,'left_marker_%perfect'].values 
    index = df.loc[:,'file_id'].values
    a = pd.Series(data = index, index = column)
    b = a.loc[0]
    
b.to_csv('H:\Practice\BadTrip.csv')            
            
    