#练习 输入十个数，输出第二大的值
#列表
listNum = []
 
num = 0 
while num < 10:
    val = int(input())
	#使用append函数输入
    listNum.append(val)
    num += 1
print(listNum)
#输入数值填充进列表

listNum.sort()
#升序排序
count = listNum.count(listNum[len(listNum) - 1])
#1.len(listNum) 计算出升序列表的长度
#2.(listNum) - 1  最后一位元素的下标
#3.listNum[len(listNum) - 1]  提取最后一位元素
#4.listNum.count(listNum[len(listNum) - 1])  计算出列表中有多少个最大值元素
#5.count = listNum.count(listNum[len(listNum) - 1])   传入count
# 删除最大值
c = 0 #计数
while c < count:
    listNum.pop() 
	#移除最后面的数
    c += 1
#拿出最后一个值 即为第二大的值
print(listNum[len(listNum) - 1])