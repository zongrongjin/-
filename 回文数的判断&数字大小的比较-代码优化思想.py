#完整语句，勿直接编译运行

num = int(input("请输入一个五位数"))
a = num % 10
b = num // 10000
if a != b:  #a 不等于 b
   print("no")  #编程思想 排除思想 一个条件符合另一个就不用判断  
				#代码优化的思想


num1 = int(input())
num2 = int(input())
num3 = int(input())


max = num1
if num2 > max:   
    max = num2  #变量的命名
if num3 > max:
    max = num3

print("max =", max)
