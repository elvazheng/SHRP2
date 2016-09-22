import pandas as pd
import numpy as np
import csv

#create two separate dataframes, one with 0s for camera confidence metrics,
#the other with good data

df = pd.read_csv('H:\CameraProbabilities\Cam&Lights.csv') 
df2 = df.set_index('file_id') 

with open('H:\CameraProbabilities\BadTripFileIDs.csv', 'rb') as f: 
    reader = csv.reader(f, delimiter = ',')
    for row in reader: 
        bad_files = row

bad_files =[int(i) for i in bad_files] 
df3 = df2.loc[bad_files] 

df4 = df2.drop(bad_files)
df3.to_csv('H:\CameraProbabilities\BadFiles&Lights.csv') 
df4.to_csv('H:\CameraProbabilities\GoodFiles&Lights.csv')
 