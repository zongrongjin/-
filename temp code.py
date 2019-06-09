#无参无返回值的函数
def myPrint():
	print("rywbl is good man")
	print("rywbl is nice man")
	print("rywbl is handsome man")
def fun1(x):
	y = 2*x + 1
	return(x,y)
	
myPrint()
myPrint()	
myPrint()
#函数定义参数和程序中参数可以重复 同C语言
for x in range(100) :
    print(fun1(x))
    x += 1