import pandas as pd
import numpy as np 

df = pd.read_csv('H:\VarOneSec.csv', error_bad_lines = False) 

x = df['vtti.lane_distance_off_center']
x = list(x.values) 

bins = [0, .1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 917] 
hist, bins = np.histogram(x, bins=bins) 

data = list(hist) 

