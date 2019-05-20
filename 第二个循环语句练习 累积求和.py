#while 语句
'''
while 表达式：
	语句
'''
#逻辑：当程序计算到while语句时 ，先计算表达式的值 如果"表达式"的值为假，结束整个while语句 
#如果"表达式"的值为真，则执行”语句“，执行完“语句”再去计算表达式的值
'''
num = 1
while num <= 6:
    print(num)
    num += 1
'''

num = 1
sum = 0
sum1 =0
while num <=7:
	print(num,sum)
	sum = sum1
	sum1 = num + sum
	print("%d+%d =%d"%(sum,num,sum1))
	num = num + 1

	