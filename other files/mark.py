import openpyxl 
import pandas as pd
import os
import datetime
import time



def attend(s):
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    sheet=date#+'_'+Hour+':'+Minute
    mode = 'a' if os.path.exists('Attendance.xlsx') else 'w'
            #s = ['Gauraang','Deep']
    f = pd.DataFrame(s)
    with pd.ExcelWriter('sample.xlsx', mode=mode) as writer:
        f.to_excel(writer, sheet_name=sheet, index=False)
