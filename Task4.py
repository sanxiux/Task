"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv


##先找到电话销售的电话
def is_xiaoshou(char):
    """判断是否包含空格"""
    if char.startswith('140'):
    	return True
    else:
        return False
zidian =[]
filename2 = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/calls.csv'    
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for i in range(len(calls)):
    	arrive = calls[i]
    	call = arrive[0]
    	if is_xiaoshou(call):
    		if(call not in zidian):
    			zidian.append(call)
ss = ""
for j in zidian:
	ss = ss + "\n" +j
# ##然后找到进行接短信和发短信的
# filename = 'C:/Users/Administrator/Desktop/cn-python-foundation-master/investigate texts and calls/ZH/texts.csv'
# phone = []
# with open(filename, 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)
print("These numbers could be telemarketers: ",ss)
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

