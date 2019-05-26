#存储5个人的年龄，求他们的平均年龄
age1 = 18
age2 = 19
age3 = 20
age4 = 21
age5 = 22
print((age1 + age2 + age3 + age4 + age5) / 5)

#列表代码优化
list = [18,19,20,21,22]
index = 0
sum = 0
while index < 5:
	sum += list[index]
	index += 1
	if index ==5 :
		print("平均年龄：%d" %(sum / 5))