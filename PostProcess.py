import pandas as pd
import numpy as np 
import glob

filenames = glob.glob('H:\Practice\*.csv') 

for f in filenames: 
    print f
    df = pd.read_csv(f, error_bad_lines = False) 
    
    df.loc[df['vtti.right_marker_probability'] < 800, ['vtti.lane_distance_off_center', 'vtti.lane_width', 'vtti.left_line_right_distance', 
    'vtti.right_line_left_distance' ]] = np.nan 
    
    df.loc[df['vtti.left_marker_probability'] < 800, ['vtti.lane_distance_off_center', 'vtti.lane_width', 'vtti.left_line_right_distance', 
    'vtti.right_line_left_distance']] = np.nan
    
    
    df.to_csv('H:\Practice' , 'w') #need to change path
