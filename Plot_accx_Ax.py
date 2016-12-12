import pandas as pd
import numpy as np
from pylab import *
from scipy import signal

'''pick random trips, and then draw plots and see the pattern of accx and Ax'''

KPH2MPS = 1/3.6
FS = 10
G2MPSS = 9.8
theList = [823294,823348,823714,1791038,2324271,2939902,4668140,4700910,5111730 ]
order = 1
figure()

for num in theList:
    df = pd.read_csv("Z:\TimeseriesExport\File_ID_"+str(num)+".csv")

    print "Y:\TimeseriesExport\File_ID_"+str(num)+".csv"   
    #print len(df)
    
    #trim file with available speed
    ismoving = df['vtti.speed_network'] > 0
    idx_first = np.where(ismoving)[0][0]
    idx_last = np.where(ismoving)[0][-1]
    try:
        df = df[idx_first:idx_last+1]
    except Exception:
        df = df[idx_first:idx_last]  
        
        
    #filter speed and accx, and generate Ax
    time = df['System.Time_Stamp']
    accx = df['vtti.accel_x']
    speed = df['vtti.speed_network']
        
    b,a = signal.butter(2,0.2)
    speedfilt = signal.filtfilt(b,a,speed)
    Ax = np.diff(speedfilt * KPH2MPS) * FS / G2MPSS
    Ax = np.insert(Ax,0,0)    
    accx = np.array(accx)
    
    index = 0
    while index < len(accx)-1:
        if accx[index] != accx[index]:
            accx[index] = (accx[index-1]+accx[index+1])/2
        index+=1
    accxfilt = signal.filtfilt(b,a,accx)
    
    #plot accx and Ax                  
    subplot(3,3,order)          
    plot(time[-2000:],accxfilt[-2000:])
    plot(time[-2000:],Ax[-2000:])
    title('shrp2_file_'+str(num),fontsize=10)  
    show() 
    order+=1

        
