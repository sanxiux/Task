"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

filename2 = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/calls.csv'    
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    zidian = {}
    for i in range(len(calls)):
    	arrive = calls[i]
    	if zidian.get(arrive[0])==None:
    		zidian.setdefault(arrive[0],int(arrive[3]))
    	else:
    		time = zidian.get(arrive[0])
    		zidian.update({arrive[0]:int(arrive[3])+int(time)})

    	if zidian.get(arrive[1])==None:
    		zidian.setdefault(arrive[1],int(arrive[3]))
    	else:
    		time = zidian.get(arrive[1])
    		zidian.update({arrive[1]:int(arrive[3])+int(time)})
    Keys = ""
    Values = ""
    for key,value in zidian.items():
    	if Keys=="":
    		Keys = key
    		Values = value
    	else:
    		if int(Values)-int(value) < 0:
    			Keys = key
    			Values = value
print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(Keys,Values))

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

