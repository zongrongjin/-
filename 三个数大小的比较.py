#从控制台输入三个数，输出较大的值
#不准使用max min

print("从控制台输入三个数，输出较大的值!")
print("不准使用max min")
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
num3 = int(input("请输入第三个数："))
if num1 > num2:
	num4 = num1
else:
	num4 = num2
if num4 > num3:
	print(num4,"比较大")	
else:
	if num1 < num2 :
		print(num3,"比较大")
	else:
		print("三个数相等")
