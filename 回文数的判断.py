#从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
#11111   12321   12221
print("从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”!")
print("Example:  11111   12321   12221")
num0 = int(input("请输入一个五位数："))
wanwei = num0 // 10000
qianwei = (num0-wanwei*10000) // 1000
baiwei = (num0-wanwei*10000-qianwei*1000) // 100
shiwei = (num0-wanwei*10000-qianwei*1000-baiwei*100) // 10
gewei = num0-wanwei*10000-qianwei*1000-baiwei*100-shiwei*10
#读取数字各个位数上的数字
#print(wanwei,qianwei,baiwei,shiwei,gewei)
if wanwei == gewei:
	if qianwei == shiwei:
		print ("这个数为回文数！")
	else:
		print("这个数不是回文数！")
else:
	print("这个数不是回文数！")
	
