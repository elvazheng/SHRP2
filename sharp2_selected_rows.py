import numpy as np
import pandas as pd
import glob

'''get the important columns of variables and generate the lead viehicle information'''

filenames = glob.glob("Y:\TimeseriesExport\*.csv") 
#filenames = ['Z:\TimeseriesExport\File_ID_821377.csv']  #run for a single fie

def main():
    for filename in filenames:
                    
        print filename
                
        df = pd.read_csv(filename, 
            usecols=['vtti.file_id','vtti.speed_network','vtti.accel_x','vtti.accel_y',
                    'vtti.gyro_z','vtti.lane_distance_off_center','vtti.left_marker_probability',
                    'vtti.right_marker_probability','TRACK1_TARGET_ID',
                    'TRACK2_TARGET_ID','TRACK3_TARGET_ID','TRACK4_TARGET_ID','TRACK5_TARGET_ID',
                    'TRACK6_TARGET_ID','TRACK7_TARGET_ID','TRACK8_TARGET_ID','TRACK1_X_POS_PROCESSED',
                    'TRACK2_X_POS_PROCESSED','TRACK3_X_POS_PROCESSED','TRACK4_X_POS_PROCESSED',
                    'TRACK5_X_POS_PROCESSED','TRACK6_X_POS_PROCESSED','TRACK7_X_POS_PROCESSED',
                    'TRACK8_X_POS_PROCESSED','TRACK1_Y_POS_PROCESSED','TRACK2_Y_POS_PROCESSED',
                    'TRACK3_Y_POS_PROCESSED','TRACK4_Y_POS_PROCESSED','TRACK5_Y_POS_PROCESSED',
                    'TRACK6_Y_POS_PROCESSED','TRACK7_Y_POS_PROCESSED','TRACK8_Y_POS_PROCESSED',
                    'TRACK1_X_VEL_PROCESSED','TRACK2_X_VEL_PROCESSED','TRACK3_X_VEL_PROCESSED',
                    'TRACK4_X_VEL_PROCESSED','TRACK5_X_VEL_PROCESSED','TRACK6_X_VEL_PROCESSED',
                    'TRACK7_X_VEL_PROCESSED','TRACK8_X_VEL_PROCESSED','computed.time_bin'])
                    
                    
        #revise the column names   
        col_names = [col for col in df]              
        for index in range(len(col_names)):
            if 'vtti.' in col_names[index]:
                col_names[index] = col_names[index].replace("vtti.","")            
        df.columns = col_names
     
        #get the trip ID    
        trip_id = filename[28:-4]
        
        #get the Vehicle ID
        temp_df = pd.read_csv('H:\SHRP2\\file_id_orderby_vhcID.csv')
        temp_fileID = temp_df.file_id
        temp_veh_ID = temp_df.vehicle_id
        veh_ID = 0
        for index in range(len(temp_df)):
            if temp_fileID[index] == int(trip_id):
                veh_ID = temp_veh_ID[index]
                break
        df.insert(1, 'veh_id', veh_ID)      

        #find lead vehicle         
        vhid,xpos,ypos,xvel = [],[],[],[]
        
        for num in range(1,9):
            vhid.append(np.array(df['TRACK'+str(num)+'_TARGET_ID']))
            xpos.append(np.array(df['TRACK'+str(num)+'_X_POS_PROCESSED']))
            ypos.append(np.array(df['TRACK'+str(num)+'_Y_POS_PROCESSED']))
            xvel.append(np.array(df['TRACK'+str(num)+'_X_VEL_PROCESSED']))
                 
        lv_id, lv_headway, lv_range_rate = [],[],[]
        
        for idx in range(len(df)):           
            ypos_row = [ypos[num][idx] for num in range(8)]          
            for number in ypos_row:
                if abs(number) == min(abs(x) for x in ypos_row if x is not None):
                    min_ypos = number                    
                    break
                else:
                    min_ypos = None
            
            if min_ypos is not None and abs(min_ypos) <2: 
                lv_idx = ypos_row.index(min_ypos)
                
                tgt_id = [vhid[num][idx] for num in range(8)]
                lv_tgt_id = int(tgt_id[lv_idx])
                lv_id.append(lv_tgt_id)
            
                xpos_row = [xpos[num][idx] for num in range(8)]
                lv_xpos = xpos_row[lv_idx]
                lv_headway.append(lv_xpos)
            
                xvel_row = [xvel[num][idx] for num in range(8)]
                lv_xvel = xvel_row[lv_idx]
                lv_range_rate.append(lv_xvel)                                           
            else:
                lv_id.append(None)
                lv_headway.append(None)
                lv_range_rate.append(None)  
                        
        df['lv_id'] = lv_id    
        df['lv_headway'] = lv_headway
        df['lv_range_rate'] = lv_range_rate 

        #drop rows with radar data
        cols = [c for c in df.columns if c[:5] != 'TRACK']
        df = df[cols]
                                                                                
        #reset variable time_bin and prndl      
        time_bin = np.array(df['computed.time_bin'])
        for index in range(len(time_bin)):
            if time_bin[index] == time_bin[index]:
                df['computed.time_bin'] = time_bin[index]           
                break                                                                                                                                                                                
                    
       #reset variable time_bin     
        time_bin = np.array(df['computed.time_bin'])
        for index in range(len(time_bin)):
            if time_bin[index] == time_bin[index]:
                df['computed.time_bin'] = time_bin[index]           
                break

        df.to_csv("W:\SHRP2\Sharp2_"+trip_id+".csv", index=None)
                                  
main()                  
                    
                    
                    