
#要排除错误的时间
timeStr=input()
#默认输入正确的时间  
#12:13:59  

timeList = timeStr.split(":")

h = int(timeList[0])
m = int(timeList[1])
s = int(timeList[2])
while h <= 24 :
	if ((h == 23) & (m == 59) & (s == 59)):
		break
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
	





