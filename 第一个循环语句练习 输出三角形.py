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
num1 = 1
srt = "*"
while num1 <=37:
	print(" "*20,num1 * srt,num1)
	num1 = num1 + 2
while num1 >= 0:
	print(" "*20,num1 * srt,num1)
	num1 -= 2