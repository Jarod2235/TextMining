import os
import pandas as pd
import csv
import numpy as np
import time
# import eventlet

data = pd.read_csv("earthquake_data.csv", encoding = 'gbk')
data = np.array(data)
os.system("cd .")

# eventlet.monkey_patch()
# time_limit = 20

old_data1 = "START_DATE = \'\'"
old_data2 = "END_DATE = \'\'"
old_data3 = "KEYWORD_LIST = [\'\']"
for i in range(52, 136):
    time = data[i][0]
    h, m, s = time.strip().split('/')
    print(h, m, s)
    new_data1 = "START_DATE = '" + h + '-' + m + '-' + s + '\''
    # s = int(s) + 1
    new_data2 = "END_DATE = '" + h + '-' + m + '-' + str(s) + '\''

    loc = data[i][6][0] + data[i][6][1]
    new_data3 = "KEYWORD_LIST = [\'" + loc + "地震\']"
    file_data = ""
    with open("./weibo/settings.py", "r", encoding = "utf-8") as f:
        for line in f:
            if old_data1 in line:
                file_data += new_data1
                file_data += "\n"
            elif old_data2 in line:
                file_data += new_data2
                file_data += "\n"
            elif old_data3 in line:
                file_data += new_data3
                file_data += "\n"
            else:
                file_data += line
    with open("./weibo/settings.py", "w", encoding = "utf-8") as f:
        f.write(file_data)
    # with eventlet.Timeout(time_limit, False):
    os.system("scrapy crawl search -s JOBDIR=crawls/search")
    old_data1 = new_data1
    old_data2 = new_data2
    old_data3 = new_data3
os.system("cls")