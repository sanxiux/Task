"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
zidian ={}
temp = 0

def Phone_Max_second(calls):
	global zidian
	global temp
	temp = 0
	for i in range(len(calls)):
		arrive = calls[i]
		if(len(zidian)==0):
			zidian = {arrive[0]:arrive[3]}
			temp = arrive[0]
		else:
			if(int(zidian.get(temp))>=int(arrive[3])):
				continue
			else:
				zidian = {arrive[0]:arrive[3]}
				temp = arrive[0]
	return zidian
filename2 = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/calls.csv'    
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    zidian = Phone_Max_second(calls)
    for k,v in zidian.items():
    	print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(k,v))

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telearrive[0] number> spent the longest arrive[3], <total arrive[3]> seconds, on the arrive[0] during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

