import pandas as pd
import numpy as np

'''find the offset value of the acc_x outliers'''
df = pd.read_csv("H:\SHRP2\shrp2.csv" ,usecols=['acc_x_min', 'acc_x_max'])

accx_min = np.array(df.acc_x_min)
accx_max = np.array(df.acc_x_max)
accx_min_n, accx_max_n = [], []
accx_min_ab, accx_max_ab = [], []

for index in range(len(accx_min)):
    if accx_min[index] >= -1:
        accx_min_n.append(accx_min[index])
        accx_max_n.append(accx_max[index])
    else:
        accx_min_ab.append(accx_min[index])
        accx_max_ab.append(accx_max[index])
        
print len(accx_min_n), len(accx_max_n), len(accx_min_ab),len(accx_max_ab)

n_min = np.mean(accx_min_n)
n_max = np.mean(accx_max_n)
n_dif = n_max - n_min
ab_min = np.mean(accx_min_ab)
ab_max = np.mean(accx_max_ab)
ab_dif = ab_max-ab_min
print 'min&max&diff of normal acc_x: ',n_min, n_max, n_dif
print 'min&max&diff of abnormal acc_x: ',ab_min, ab_max, ab_dif
print 'min&max offset value of acc_x: ',n_min-ab_min, n_max-ab_max

#Result:
#min&max&diff of normal acc_x:  -0.352178546366 0.29469443609 0.646872982456
#min&max&diff of abnormal acc_x:  -5.21753773585 -4.58927735849 0.628260377358
#min&max offset value of acc_x:  4.86535918948 4.88397179458
