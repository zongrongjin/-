#时间下一秒 
'''
输入一个时间字符串，输出这个时间的下一秒
12:12:23       12:12:24
12:13:59       12:14:00
'''
#要排除错误的时间
timeStr=input()
#默认输入正确的时间  
#12:13:59  

timeList = timeStr.split(":")

h = int(timeList[0])
m = int(timeList[1])
s = int(timeList[2])

s += 1
if s == 60:
	m += 1
	s = 0
	if m == 60:
		h += 1
		m = 0
		if h == 24:
			h = 0
print("%.2d:%.2d:%.2d"%(h,m,s))
	





