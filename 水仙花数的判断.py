#练习1 
'''
从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
153=1^3+5^3+3^3
'''
print("从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”!")
print("水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）")
num1 = int(input("请输入一个三位数："))
baiwei = num1 // 100
shiwei = (num1 -baiwei*100) //10
gewei = num1 - (shiwei * 10 + baiwei * 100)
#获取数字的个位 十位 百位上的数字
#print(baiwei,shiwei,gewei)
sxh1 = pow(gewei,3) + pow(shiwei,3) + pow(baiwei,3)
#求取对应的水仙花数
if num1 == sxh1:
	print("您输入的数为水仙花数！")
else:
	print("您输入的数不是水仙花数！")
	