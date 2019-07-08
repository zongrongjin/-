#写文件的一种有效方式
try:
	path = r"D:\文档\2019.6\python工作文件夹\Result.txt"
	f = open(path,"a+",encoding = "UTF-8-sig")
	# Force = mass *  acceleration  
	# Mass = massZero /sqrt(1 - velocity * velocity / VelocityLight * VelocityLight)
	# velocityTime = velocityZero + acceleration * time
	#Part 0  定义常量
	timeZero = 0
	velocityZero = 0
	acceleration  = 1   #m2/s
	VelocityLight = 299792458 #m2/s
	#Part 1  定义变量
	velocityTime = 0
	time = 0
	#Part 1  录入基本公式
	#Part 1.1 录取最简单的vt = v0 + at
	f.write("v0:%d a:%d \n"%(velocityZero,acceleration))
	for time in range(2997925):
		velocityTime = velocityZero + acceleration * time
		f.write("vt:%d t:%d\n"%(velocityTime,time))
	f.close()
finally:
    if f:
        f.close()	
