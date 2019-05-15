#不准使用max min
#从控制台输入两个数，输出较大的值
print("从控制台输入两个数，输出较大的值!")
print("不准使用max min")
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
if num1 > num2:
	print(num1,"比较大")	
else:
	if num1 < num2 :
		print(num2,"比较大")
	else:
		print("两个数相等")
