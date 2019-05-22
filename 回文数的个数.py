#输出五位数中回文数的个数
print("输出五位数中回文数的个数!")
num = 0
num0 = 10000
while num0 <= 99999:
	wanwei = num0 // 10000
	qianwei = (num0-wanwei*10000) // 1000
	baiwei = (num0-wanwei*10000-qianwei*1000) // 100
	shiwei = (num0-wanwei*10000-qianwei*1000-baiwei*100) // 10
	gewei = num0-wanwei*10000-qianwei*1000-baiwei*100-shiwei*10
	if ((wanwei == gewei)&(qianwei == shiwei)):
		num += 1
	num0 += 1
print(num)
