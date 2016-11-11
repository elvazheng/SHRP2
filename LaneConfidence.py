import pandas as pd
import numpy as np
import glob


filenames = glob.glob('H:\Practice\*.csv') 

frame_list = []
for filename in filenames: 
    print filename
    df = pd.read_csv(filename, usecols=['vtti.file_id', 'vtti.left_marker_probability',
                'vtti.right_marker_probability', 'vtti.left_line_right_distance', 
                'vtti.right_line_left_distance', 'vtti.lane_distance_off_center', 'vtti.lane_width' ],
                error_bad_lines=False) 

    file_id = int(df['vtti.file_id'][:1])

    f_list = []
    df_id = pd.DataFrame([[int(file_id)]],columns = ['file_id'])
    f_list.append(df_id)
     
   
    for col in df: 
        column = df[col] 
        total_rows = len(column) 
        total_non_zero = (column != 0).sum()
        percent_non_zero = total_non_zero / total_rows * 100
        rows = np.array(percent_non_zero)  
    
    
    columns = ['left_marker_probability_%miss', 'right_marker_probability_%miss', 'left_line_right_distance_%miss',
    'right_line_left_distance_%miss', 'lane_distance_off_center_%miss', 'lane_width_%miss'] 
    f = pd.DataFrame(rows, columns = columns)
    f_list.append(f)   
    
    frame = pd.concat([f for f in f_list],axis=1) 
    frame_list.append(frame)
    
                       
new_frame = pd.concat(frame_list,axis=0)

#new_frame.to_csv('H:\Camera%Useable\CameraPercentUseable.csv', index=None)    
    
    

     
    
    
    
        
        

    
    
        
        
            
            
            
            
            
            
            
            
        
             
            
        
            
            
        
                
         
            
        
        
        
        
        

    
