#作业讲解
#练习1 计算水仙花数
num = int(input("请输入一个三位数"))
#153
a = num % 10
b = num // 10 % 10 #灵活应用取整和取余函数
c = num // 100

if num == a**3 + b**3 + c**3:   #复合运算符的使用
    print("yes")
else:
    print("no")	
