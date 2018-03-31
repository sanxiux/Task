"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
filename = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/texts.csv'
phone = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for i in range(len(texts)):
    	arrive = texts[i]
    	if arrive[0] not in texts:
    		phone.append(arrive[0])
    	if arrive[1] not in texts:
    		phone.append(arrive[1])
print ("There are {} different telephone numbers in the records.".format(len(phone)))

filename2 = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/calls.csv'    
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for i in range(len(calls)):
    	arrive2 = calls[i]
    	if arrive2[0] not in calls and phone:
    		phone.append(arrive2[0])
    	if arrive2[1] not in calls and phone:
    		phone.append(arrive2[1])
print ("There are {} different telephone numbers in the records.".format(len(phone)))
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
