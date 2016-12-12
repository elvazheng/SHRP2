import pandas as pd
import numpy as np
import glob

'''statistics of shrp2 data, including min, max, mean, median, %miss of each variable'''

filenames = glob.glob("Y:\TimeseriesExport\*.csv")      


frame_list = []

for filename in filenames:    
    
    print filename
    df = pd.read_csv(filename, 
         usecols=['vtti.timestamp', 'vtti.file_id', 'computed.time_bin', 'vtti.alcohol_interior', 
                'vtti.light_level', 'vtti.steering_wheel_position', 'vtti.pedal_gas_position', 
                'vtti.pedal_brake_state', 'vtti.cruise_state', 'vtti.speed_network', 
                'vtti.accel_x','vtti.accel_y', 'vtti.gyro_z', 'vtti.left_line_right_distance', 
                'vtti.right_line_left_distance', 'vtti.speed_gps', 
                'vtti.head_confidence', 'TRACK1_X_POS_PROCESSED','TRACK1_X_VEL_PROCESSED'],
                error_bad_lines=False)
    file_id = int(df['vtti.file_id'][:1])

    f_list = []
    df_id = pd.DataFrame([[int(file_id)]],columns = ['file_id'])
    f_list.append(df_id)

    for col in df:  
        if (col != 'vtti.timestamp') and (col != 'vtti.file_id'):
            df_col = df[col]                                  
            minimum = np.amin(df_col)
            maximum = np.amax(df_col)
            mean = np.mean(df_col)
            median = np.median(df_col[df_col.notnull()])
            miss = (len(df) - df_col.count())/float(len(df)) 
                                                            
            data = np.array([[minimum, maximum, mean, median, miss]])    
            columns = [col[:]+'_min',col[:]+'_max',col[:]+'_mean',col[:]+'_median',col[:]+'_%miss']
            f = pd.DataFrame(data, columns=columns)  
            f_list.append(f)   
    frame = pd.concat([f for f in f_list],axis=1) 
    frame_list.append(frame)
    
#concatenate all files                       
allframe = pd.concat(frame_list,axis=0)   
print 'len of allframe', len(frame_list)    
    
#revise the column names
col_names = [col for col in allframe]              
for index in range(len(col_names)):
    if 'computed.time_bin' in col_names[index]:
        col_names[index] = col_names[index].replace("computed.","")
    elif 'vtti.alcohol' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.alcohol_interior","alcohol")
    elif 'vtti.light_level' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.light_level","light")
    elif 'vtti.steering_wheel' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.steering_wheel_position","steering")
    elif 'vtti.pedal_gas_position' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.pedal_gas_position","pedal_gas")
    elif 'vtti.pedal_brake_state' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.pedal_brake_state","brake")
    elif 'vtti.cruise_state' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.cruise_state","cruise")
    elif 'vtti.speed_network' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.speed_network","spd_net")
    elif 'vtti.accel_x' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.accel_x","acc_x")
    elif 'vtti.gyro_z' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.gyro_z","gyro_z")
    elif 'vtti.left_line_right_distance' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.left_line_right_distance","lft_rgt_dist")
    elif 'vtti.right_line_left_distance' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.right_line_left_distance","rgt_lft_dist")
    elif 'vtti.speed_gps' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.speed_gps","speed")
    elif 'vtti.head_confidence' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.head_confidence","head_conf")
    elif 'TRACK1_X_POS_PROCESSED' in col_names[index]:
        col_names[index] = col_names[index].replace("TRACK1_X_POS_PROCESSED","T1x_pos")
    elif 'TRACK1_X_VEL_PROCESSED' in col_names[index]:
        col_names[index] = col_names[index].replace("TRACK1_X_VEL_PROCESSED","T1x_vel") 
    elif 'vtti.accel_y' in col_names[index]:
        col_names[index] = col_names[index].replace("vtti.accel_y","acc_y")                                               
allframe.columns = col_names



#add participantID and VehicleID columns
id_df = pd.read_csv("H:\SHRP2\Insight_Westat.csv" ,usecols=['displayTripID','anonymousParticipantID','anonymousVehicleID'])
print 'len of id_df', len(id_df)

tripID = np.array(id_df.displayTripID)
participantID = np.array(id_df.anonymousParticipantID)
vehicleID = np.array(id_df.anonymousVehicleID)
partic_id, vehicle_id = [], []

for fileID in np.array(allframe.file_id):
    for index in range(len(id_df)):
        if fileID == tripID[index]:
            partic_id.append(participantID[index])
            vehicle_id.append(vehicleID[index])
            break


allframe.insert(1,'partic_id',partic_id)
allframe.insert(2,'vehicle_id',vehicle_id)

#save frames to csv
allframe.to_csv("H:\SHRP2\shrp2.csv", index=None)
#allframe.to_csv("H:\SHRP2\shrp2_test.csv", index=None)      #test
   
            
            