#练习 输入十个数，输出第二大的值
#列表
#课堂练习
listNum = []
 
num = 0 
while num < 5:
    val = int(input("请输入第%d个数:  " %(num+1)))
	#使用append函数输入
	#优化输入格式
    print("您输入的第%d个数字为%d。"%(num+1 , val))
    listNum.append(val)
    num += 1
print("您输入的列表为： ",listNum)  
#提示并输出初始列表
#输入数值填充进列表


if listNum[0] >= listNum[1]:
    max = listNum[0]
    sec = listNum[1]
else:
    max = listNum[1]
    sec = listNum[0]
	
index = 2
while index < len(listNum):
    if listNum[index] >= sec:
        sec = listNum[index]
    if listNum[index] >= max:
        sec = max
        max = listNum[index]
    index += 1

print(sec)

#有等于会异常