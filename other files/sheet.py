from openpyxl import *
import pandas as pd
import os
import datetime
import time


ts = time.time()      
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
Hour,Minute,Second=timeStamp.split(":")
sheet=date#+'_'+Hour+':'+Minute


mode = 'a' if os.path.exists('sample.xlsx') else 'w'
for i in range(1,4):
        s = ['Gauraang','Deep']
        f = pd.DataFrame(s)
        with pd.ExcelWriter('sample.xlsx', mode='a') as writer:
            f.to_excel(writer, sheet_name=sheet, index=False)

        i=i+1
