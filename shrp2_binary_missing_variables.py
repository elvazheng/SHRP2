import pandas as pd
import numpy as np

'''record the trips that contain 100%-missing variables, sorted by vhicle_id and partic_id'''

df_orig = pd.read_csv("H:\SHRP2\shrp2.csv" ,usecols=['partic_id','vehicle_id',
                    'steering_%miss','pedal_gas_%miss','brake_%miss',
                    'cruise_%miss','acc_x_min'])   #set <-1 as the threshold of acc_x_min
                    
df = df_orig.sort_values(by=['vehicle_id','partic_id'])                    
#print df[0:5]

steering = np.array(df['steering_%miss'])
throttle = np.array(df['pedal_gas_%miss'])
brake = np.array(df['brake_%miss'])
cruise = np.array(df['cruise_%miss'])
acc = np.array(df['acc_x_min'])
drop_list = []

#drop trips that has no 100% missing value in every variable
for index in range(len(df)):
    if (steering[index] !=1 and throttle[index] !=1 and brake[index] !=1 and cruise[index] !=1 and acc[index] >-1):
        drop_list.append(index)

df = df.drop(df.index[drop_list])

#exchange to binary
for col in df:
    if (col == 'partic_id' or col == 'vehicle_id' or col == 'acc_x_min'):
        continue
    else:
        df[col][df[col] !=1] = 0 
df.acc_x_min[df.acc_x_min >-1] =0 
df.acc_x_min[df.acc_x_min < -1] =1
 
#drop duplicate lines 
df = df.drop_duplicates(keep = 'first')  

#revise column names    
col_names = [col.replace('%','') for col in df]  
col_names[-1] = 'acc_x_outlier'             
df.columns = col_names    
    
df.to_csv("H:\SHRP2\shrp2_binary_miss_variables.csv", index=None)
