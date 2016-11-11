import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('H:\Giantframe.csv', error_bad_lines= False)

#compute standard deviation in groups of 10 rows
y= df['vtti.lane_distance_off_center'].groupby(df.index/10).std() 
   
#compute average probability in groups of 10 rows            
x_value_frame = df[(['vtti.left_marker_probability', 'vtti.right_marker_probability'])].groupby(df.index/10).mean()
    
#take the larger of the two average probabilities for our x coordinate
x_value_frame['larger_probability'] = x_value_frame[['vtti.left_marker_probability','vtti.right_marker_probability']].max(axis=1) 
x = pd.Series(data=x_value_frame['larger_probability'])
 
#plt.scatter(x=x,y=y)
#plt.show()
      
                      
#create a new dataframe with x,y coordinates 
df2 = pd.concat([x,y], axis=1)
df2.to_csv('H:\VarOneSec.csv') 

