#打印出所有三位数中的水仙花数
print("打印出所有三位数中的水仙花数!")
num = 100
while num <= 999:
	a = num % 10
	b = num // 10 % 10 #灵活应用取整和取余函数
	c = num // 100
	if num == a**3 + b**3 + c**3: 
		print(num)
	num += 1