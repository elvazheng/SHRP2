import pandas as pd
import numpy as np
import glob 
import csv

filenames = glob.glob('Y:\TimeseriesExport\*.csv') 
frame_list = [] 

for filename in filenames:
    #pass files with all NaNs in camera confidence columns
    with open('H:\Nulls.csv', 'rb') as f: 
     reader = csv.reader(f, delimiter= ',') 
     for row in reader: 
        skip = row
        skip = ['Y:\TimeseriesExport\File_ID_' + i for i in skip] 
        if filename != skip: 
            continue     

    df = pd.read_csv(filename, usecols= ['vtti.file_id','vtti.left_marker_probability',
                'vtti.right_marker_probability', 'vtti.light_level'], error_bad_lines = False, low_memory= False) 
    
    print filename            
    
    file_id = float(df['vtti.file_id'][:1])
    f_list = []
    df_id = pd.DataFrame([[int(file_id)]],columns = ['file_id'])
    f_list.append(df_id)
    
    #Create the new dataframe with camera confidence metrics for each trip in the dataset 
    for col in df: 
        if col == ('vtti.left_marker_probability'): 
            column = df[col] 
            mean_left = np.mean(column) 
            standard_deviation_left = np.std(column) 
            unique_values_left = column[(column == 1024)] 
            percentage_perfect_left = float(len(unique_values_left)) / float(len(column))  * 100 #% of the time machine vision is full
            left_cam_rows = np.array([mean_left, standard_deviation_left, percentage_perfect_left]) 
                         
        if col == ('vtti.right_marker_probability'): 
            column = df[col] 
            mean_right = np.mean(column) 
            standard_deviation_right = np.std(column) 
            unique_values_right = column[(column == 1024)] 
            percentage_perfect_right = float(len(unique_values_right)) / float(len(column)) * 100
            right_cam_rows = np.array([mean_right, standard_deviation_right, percentage_perfect_right])
    
    #add ambient light level metrics to the dataframe 
    for col in df:    
        if col == ('vtti.light_level'): 
            column = df[col] 
            light_min = np.amin(column)           
            light_max = np.amax(column)
            light_rows = np.array([light_min,light_max])    
            rows = np.hstack([left_cam_rows, right_cam_rows, light_rows]) 
            columns = ['left_marker_mean', 'left_marker_stdv', 'left_marker_%perfect',
        'right_marker_mean', 'right_marker_stdv','right_marker_%perfect', 'light_min','light_max'] 
             
            
            a = pd.DataFrame(rows, index=columns) 
            f = a.T #transpose the dataframe before concatinating all trips in the dataset
            f_list.append(f)   
    
    frame = pd.concat([f for f in f_list],axis=1) 
    frame_list.append(frame)
    new_frame = pd.concat(frame_list,axis=0)           
    new_frame.to_csv('H:\CameraProbabilities\Cam&Lights.csv',index=None) 

            
            
            
             
        
            
            
            
    
    
        
