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
'''
'''
#输出字符串中的每个字符。
index = 0
str = "No description, website, or topics provided."
#print(len(str))
while index < len(str):
	print("str[%d] =%s" %(index,str[index]))
	index +=1
'''	
#ascii码转换
'''
str ='a'
print(ord(str))
print(chr(66))
'''
#ascii码打印
num = ord('A')
while num <= ord('z'):
	print (num,chr(num))
	num += 1
