# -*- coding: cp949 -*-
import glob
import xlrd
import csv
import sys
import codecs
from importlib import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')

xlfiles=glob.glob(r'C:\Users\user\Desktop\store_region/*.xls')

wf=csv.writer(codecs.open(r'C:\Users\user\Desktop\store_region/map.csv','w','utf-8'),delimiter=',')

for files in xlfiles:
    print(files)
    workbook=xlrd.open_workbook(files)
    sheet=workbook.sheet_by_index(0)
    
    for row in range(2,sheet.nrows):
        wf.writerow(sheet.row_values(row))
