#练习 输入十个数，输出第二大的值
#列表
#课堂练习
listNum = []
 
num = 0 
while num < 10:
    val = int(input("请输入第%d个数:  " %(num+1)))
	#使用append函数输入
	#优化输入格式
    print("您输入的第%d个数字为%d。"%(num+1 , val))
    listNum.append(val)
    num += 1
print("您输入的列表为： ",listNum)  
#提示并输出初始列表
#输入数值填充进列表

listNum.sort()
#升序排序
print("升序排序后的列表为：",listNum)
count = listNum.count(listNum[len(listNum) - 1])
#1.len(listNum) 计算出升序列表的长度
print("计算出升序列表的长度为：",len(listNum))
#2.(listNum) - 1  最后一位元素的下标
#3.listNum[len(listNum) - 1]  提取最后一位元素
print("提取最后一位元素为：%d"%(listNum[len(listNum) - 1]))
#4.listNum.count(listNum[len(listNum) - 1])  计算出列表中有多少个最大值元素
print("计算出列表中有%d个最大值元素"%(listNum.count(listNum[len(listNum) - 1])))
#5.count = listNum.count(listNum[len(listNum) - 1])   传入count
# 删除最大值
c = 0 #计数
while c < count:
    print("移除的最大的数为%d"%(listNum.pop()))
    listNum.pop() 
	#移除最后面的数
    c += 1
#拿出最后一个值 即为第二大的值
print(listNum[len(listNum) - 1])