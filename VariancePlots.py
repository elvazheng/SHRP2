import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


#for every 10 values of system time, plot the greater of the average of marker probabilities and variance of lane offset


df = pd.read_csv('H:\Practice\File_ID_821377.csv', usecols = ['vtti.left_marker_probability', 
'vtti.right_marker_probability', 'vtti.lane_distance_off_center'], error_bad_lines=False)

variance_frame= df['vtti.lane_distance_off_center'] 
y_values = variance_frame.groupby(df.index/10).var()
y = y_values.dropna() 

x_value_frame = df[['vtti.left_marker_probability', 'vtti.right_marker_probability']] 
x_values = x_value_frame.groupby(df.index/10).mean()
x_values['larger_probability'] = x_values[['vtti.left_marker_probability','vtti.right_marker_probability']].max(axis=1) 
x = pd.Series(data=x_values['larger_probability']).dropna() 

plt.scatter(x,y)  
plt.show()
