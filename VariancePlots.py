import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

filenames = glob.glob('Y:\TimeSeriesExport\*.csv') 
#for every 10 values of system time, plot the greater of the average of marker probabilities and variance of lane offset
for filename in filenames:     
    print filename
    
    #drop nAn's after reading in CSV's 
    df = pd.read_csv(filename, usecols = ['vtti.left_marker_probability', 
    'vtti.right_marker_probability', 'vtti.lane_distance_off_center'], error_bad_lines=False).dropna()
    
    #compute standard deviation in groups of 10 rows
    variance_frame= df['vtti.lane_distance_off_center'] 
    y = variance_frame.groupby(df.index/10).std()
        
    x_value_frame = df[(['vtti.left_marker_probability', 'vtti.right_marker_probability'])]
    #compute average probability in groups of 10 rows
    x_value_frame = x_value_frame.groupby(df.index/10).mean()
    #take the larger of the two average probabilities for our x coordinate
    x_value_frame['larger_probability'] = x_value_frame[['vtti.left_marker_probability','vtti.right_marker_probability']].max(axis=1) 
    x = pd.Series(data=x_value_frame['larger_probability'])
    

    df2 = pd.concat([x,y], axis=1).reset_index()
    df2.to_csv('H:\Var.csv') 