"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv


#这是所有的播出电话号码
zidian_first =[]
#这是接听电话的
zidian_second = []
#这个是发短信的
zidian_third = []
#这个是接收短信的
zidian_forth = []
filename2 = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/calls.csv'    
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for i in range(len(calls)):
        arrive = calls[i]
        if arrive[0] not in zidian_first:
            zidian_first.append(arrive[0])
        if arrive[1] not in zidian_second:
            zidian_second.append(arrive[1])

filename = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/texts.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for i in range(len(texts)):
        arrive = texts[i]
        if arrive[0] not in zidian_third:
            zidian_third.append(arrive[0])
        if arrive[1] not in zidian_forth:
            zidian_forth.append(arrive[1])

tmp = [val1 for val1 in zidian_first if val1 not in zidian_second]
tmp2 = [val2 for val2 in tmp if val2 not in zidian_third]
tmp3 = sorted([val3 for val3 in tmp2 if val3 not in zidian_forth])

print("These numbers could be telemarketers")
for tp in tmp3:
    print(tp)
"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

