"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import string
zidian ={}
##返回的是第一个问题的
def Phone_Max_second(key,value):
	global zidian
	if(len(zidian)==0):
		zidian.setdefault(key,value)
	elif key in zidian.keys():
		zidian[key] = (zidian[key]+','+value)
	else:
		zidian.setdefault(key,value)


def is_contain(char):
    if char.find('(080)')!=-1:
    	return True
    else:
        return False
def is_space(char):
    if char.find(' ')!=-1:
    	return True
    else:
        return False
def is_kuohao(char):
    if char.find('(')!=-1:
    	return True
    else:
        return False
def is_xiaoshou(char):
    """判断是否包含空格"""
    if char.startswith('140'):
        return True
    else:
        return False
zidian_first = []
zong = 0
quan = 0
filename2 = 'calls.csv'   
with open(filename2, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for i in range(len(calls)):
        arrive = calls[i]
        if is_contain(arrive[0]):
            zong +=1
            if is_contain(arrive[1]):
                quan +=1
                
            if is_space(arrive[1]):
                One = arrive[1][:arrive[1].find(' ')-1]
                if One not in zidian_first:
                    zidian_first.append(One)
                continue
            if is_kuohao(arrive[1]):
                Two = arrive[1][:arrive[1].find(')')+1]
                if Two not in zidian_first:
                    zidian_first.append(Two)
                    continue
            if is_xiaoshou(arrive[1]):
                third = arrive[1][:arrive[1].find(')')+1]
                if third not in zidian_first:
                    zidian_first.append(third)
                    continue
percent = float(quan)/float(zong) *100

print("The numbers called by people in Bangalore have codes:")
for tp in sorted(zidian_first):
    print(tp)


print("\n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percent,2)))
"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>.
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

##本地打给本地的占所有电话的比例  然后用百分比fload 


输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
