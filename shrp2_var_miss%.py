import pandas as pd
import numpy as np

'''in all 2048 trips, how many percent of each variable is totally missing'''
'''eg. if one trip has no steering data, then the steering data is totally missing'''

df = pd.read_csv("H:\SHRP2\shrp2.csv" ,usecols=['time_bin_%miss','alcohol_%miss',
                'light_%miss','steering_%miss','pedal_gas_%miss','brake_%miss',
                'cruise_%miss','spd_net_%miss','acc_x_%miss','gyro_z_%miss',
                'lft_rgt_dist_%miss','rgt_lft_dist_%miss','speed_%miss',
                'head_conf_%miss','T1x_pos_%miss','T1x_vel_%miss'])

col_list= [col for col in df]                
percent_list = []
len_df = len(df)

for col in df:                
    a = np.count_nonzero(np.array(df[col])==1)
    percent_list.append(a/float(len_df))

data = np.array([col_list,percent_list]).T
col = ['variables', '%_miss']
f = pd.DataFrame(data, columns = col)
print f
    
f.to_csv("H:\SHRP2\shrp2_var_miss%.csv", index=None)
