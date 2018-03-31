"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
filename = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/texts.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    element_First = texts[0]
    print('First record of texts,{} texts {} at time {}'.format(element_First[0],element_First[1],element_First[2]))


filename2 = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/calls.csv'    
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    element_Last = calls[-1]
    print('Last record of calls,{} calls {} at time {}, lasting {} seconds'.format(element_Last[0],element_Last[1],element_Last[2],element_Last[3]))


"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

