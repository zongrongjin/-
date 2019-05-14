'''


#num1 = int(input("请输入一个数："))
#num2 = int(input("请输入另一个数："))
#print("num1 + num2 =",num1 + num2)
#del 删除变量

a = 1
del a
age = 18.8

print(type(age))
#查看变量的类型
print(age)	
#查看变量的值
print(id(age))
#查看变量的地址

#定义变量

#常量 程序运行期间不能改变的数据为常量

#数字的分类:整数 浮点数 复数

#整数 
#Python可以处理任意大小的整数，当然包括负数，在程序中的写法和数学相同

#连续定义多个变量

num1 = 1
num2 = 2
print(num1,num2)
#连续定义多个变量
num3 = num4 = num5 = 4
print(num3,num4,num5)
#连续定义多个变量*1
#交互式赋值定义变量
num6,num7 = 6,7
num8 = num1
print(num6,num7)
#整数的定义
print(1001,id(num1),1002,id(num2),1003,id(num3),1004,id(num4),1008,id(num8))
#观察变量的内存值变化  全局变量的问题 标识全局变量
#Python的作用域  地址和堆栈


#浮点型
#浮点型由整数和小叔部分组成
#浮点数运算可能有四舍五入的误差 Maybe
#后续分析
f1 = 1.1
f2 = 2.2
print(f1+f2)

#复数 实数部分和虚数部分组成的可以用a + bj


#数字类型转换
#将浮点型转为整数 int()   
print(int(1.1),int(1.9))
#向下取整
#转换为小数 float()
print(float(1))
#字符串转整数
print(int("123"))
#字符串转小数
print(float("123"))
#+-号作为正负号有意义
print(int("+123"))
print(int("-123"))
#print(int("abc"))
#print(int("123abc"))
#int 转整数需要符合一定的规格


#数学函数
#绝对值函数 abs()  返回数字的绝对值
a1 = -10
a2 =abs(a1)  
print(a1,a2,abs(a1))

#比较两个数的大小
a3 = 100
a4 = 9
print((a3>a4)-(a3<a4))

a3 = 1
a4 = 9
print((a3>a4)-(a3<a4))

a3 = 9
a4 = 9
print((a3>a4)-(a3<a4))

#返回给定参数的最大值  数字个数无所谓
print(max(1,2,3,4,5,6,7,8))
#返回给定参数的最小值
print(min(1,2,3,4,5,6,7,8))

#求x的y次方 pow() power 2^5  常量和变量都可以
print(pow(2, 5))

#round(x,[n])返回浮点数x的四舍五入的值，如果给出n值，则代表舍入到小数点后n位
print(round(3.456))
print(round(3.556))
print(round(3.456, 2))
print(round(3.546, 1))



#导入一个库：封装一些功能   math 数学相关的库
print(math.ceil(18.1))
print(math.ceil(18.9))
#向上取整
print(math.floor(18.1))
print(math.floor(18.9))
'''
import math
import random
#math.modf(22.3) 返回整数部分和小说部分 整数部分和小数部分都为浮点数 元组
print(math.modf(22.3))
#开方 返回结果为浮点数
print(math.sqrt(225))

#随机数函数 导入random库 序列（列表）
print(random.choice([1,2,3,4,5]))
#1从序列的元素中随机挑选一个元素  不局限为数字
print(random.choice(range(5)))
#range(5) == [0,1,2,3,4]  程序的执行程序 由内到外 
print(random.choice("sunck"))
#"sunck"  == ["s","u","n","c","k"]

#产生一个1~100之间的随机数
r1 = random.choice(range(100)) + 1
print(r1)
#彩票系统
#判断是否中奖   num == res

#从指定范围内，按指定的基数递增的集合中选取一个随机数
#random.randrange([start,] stop[, step])  []非必须参数
#start--指定范围的开始值，包含在范围内，默认是0
#stop--指定范围的结束之，不包含在范围内
#step--指定的递增基数，默认是1
print(random.randrange(1, 100, 2))
#从0-99选取一个随机数
print(random.randrange(100))

#随机生产[0,1)之间的数(浮点数)
print(random.random())


list = [1,2,3,4,5]
#将序列的所有元素随机排序
random.shuffle(list)
print(list)


#随机生产一个实数，他在[3,9]范围
print(random.uniform(3,9))
