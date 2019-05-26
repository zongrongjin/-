#字符串中数字部分求和
print("字符串中数字部分求和")
str = input("请输入一个混合字符串")
index = 0
sum = 0
while index < len(str):
	if str[index] >= "0" and str[index] <= "9":
		sum += int(str[index])
	index += 1
print("sum = %d" %(sum))

