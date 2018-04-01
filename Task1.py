"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
filename = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/texts.csv'
phone = []
news_ids = []
def news_phone(lists):
	global news_ids
	for id in lists:
	    if id not in news_ids:
	        news_ids.append(id)

with open(filename, 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for i in range(len(texts)):
    	arrive = texts[i]
    	phone.append(arrive[0])
    	phone.append(arrive[1])

filename2 = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/calls.csv'    
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for i in range(len(calls)):
    	arrive2 = calls[i]
    	phone.append(arrive2[0])
    	phone.append(arrive2[1])
news_phone(phone)
print ("There are {} different telephone numbers in the records.".format(len(news_ids)))
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
