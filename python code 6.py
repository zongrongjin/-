#时间下一秒   歌词解析   练习
'''
set:类似dict，是一组key的集合，不存储value

本质：无序和无重复元素的集合
'''

#创建
#创建set需要一个list或者tuple或者dict作为输入集合
#重复元素在set中会自动被过滤
s1 = set([1,2,3,4,5,3,4,5])
print(s1)   #用list创建set
# dict set都用大括号表示 
s2 = set((1,2,3,3,2,1))  #使用元组
print(s2)   #有重复值自动去重 
s3 = set({1:"good", 2:"nice"})
print(s3) #使用字典   
#字典无序，无法用下标取值，只能用Key取值


#添加
s4 = set([1,2,3,4,5])
s4.add(6)
s4.add(3) #可以添加重复的，但是不会有效果
#s4.add([7,8,9]) #set的元素不能是列表，因为列表是可变的
s4.add((7,8,9))  #元组不可变，所以可以添加
#s4.add({1:"a"}) #set的元素不能是字典，因为字典是可变的
print(s4)


#插入整个list、tuple、字符串，打碎插入
s5 = set([1,2,3,4,5])
s5.update([6,7,8]) #list
s5.update((9,10))  #tuple
s5.update("sunck")  #str
print(s5)


#删除
s6 = set([1,2,3,4,5])
s6.remove(3)
print(s6)



#遍历
s7 = set([1,2,3,4,5])
for i in s7:
    print(i)
#set没有索引的
#print(s7[3])

for index, data in enumerate(s7):
    print(index, data)


s8 = set([1,2,3])
s9 = set([2,3,4])
#交集
a1 = s8 & s9
print(a1)
print(type(a1))
#并集
a2 = s8 | s9
print(a2)
print(type(a2))

#类型转换
#list-->set
l1 = [1,2,3,4,5,3,4,5]
s1 = set(l1)


#tuple-->set
t2 = (1,2,3,4,3,2)
s2 = set(t2)


#set-->list
s3 = {1,2,3,4}
l3 = list(s3)
print(l3)

#set-->tuple
s4 = {2,3,4,5}
t4 = tuple(s4)
print(t4)
#借助set来去重

l = [1,2,3,4,3,4,5,6]
'''
s = set(l)
l = list(s)
print(l)
'''

l = list(set(l))
print(l)


#迭代器
#包的引入
'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象(Iterable)。
可以用isinstance()去判断一个对象是否是Iterable对象
 #使用前需引入一个包  from  collections import Iterable
可以直接作用于for的数据类型一般分两种
	1、集合数据类型，如list、tuple、dict、set、string
	2、是generator，包括生成器和带yield的generator function
'''
from  collections import Iterable
from  collections import Iterator
'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象(Iterable)。
可以用isinstance()去判断一个对象是否是Iterable对象

可以直接作用于for的数据类型一般分两种
1、集合数据类型，如list、tuple、dict、set、string
2、是generator，包括生成器和带yield的generator function
'''
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(1, Iterable))




'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后跑出一个StopIteration错误表示无法继续返回下一个值
可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)


可以使用isinstance()函数判断一个对象是否是Iterator对象

'''
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))
#只有最后一个为迭代器

l = (x for x in [23,4,5,64,3435])
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))


#转成Iterator对象
a = iter([1,2,3,4,5])
print(next(a))
print(next(a))
#list tuple dict str
print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(''), Iterator))


#错误处理


凯 = "帅"  #汉字也可以做变量
print(凯)

'''
认识函数：在一个完整的项目中，某些功能会反复的使用。那么会将功能封装成函数，
当我们要使用功能的时候直接调用函数即可

本质：函数就是对功能的封装

优点
1、简化代码结构，增加了代码的复用度(重复使用的程度)
2、如果想修改某些功能或者调试某个BUG，还需要修改对应的函数即可
'''




'''
定义函数：

格式：
def 函数名(参数列表):
    语句
    return 表达式


def:函数代码块以def关键字开始
函数名：遵循标识符规则
():是参数列表的开始和结束
参数列表(参数1,参数2,……,参数n):任何传入函数的参数和变量必须放在圆括号之间，用逗号分隔。函数从函数的调用者哪里获取的信息
冒号：函数内容(封装的功能)以冒号开始，并且缩进
语句：函数封装的功能
return：一般用于结束函数，并返回信息给函数的调用者
表达式：即为要返回给函数的调用者的信息，

注意：最后的return 表达式，可以不写，相当于return None
'''

'''
凯 = "帅"
print(凯)
'''



'''
函数的调用
格式：函数名(参数列表)

函数名：是要使用的功能的函数函数名字
参数列表：函数的调用者给函数传递的信息,如果没有参数，小括号也不能省略

函数调用的本质：实参给形参赋值的过程

'''
#无参无返回值的函数
def myPrint():
	print("rywbl is good man")
	print("rywbl is nice man")
	print("rywbl is handsome man")
	
myPrint()
myPrint()	
myPrint()

#编写函数，实现功能，给函数两个数，返回这两个数的和


def mySum(num1, num2):
    #将结果返回给函数的调用者
    return num1 + num2
    #执行完return语句，该函数就结束了，return后面的代码不执行
    print("**********")

res = mySum(1, 2)
print(res)



'''
值传递：传递的不可变类型
string、tuple、number是不可变的
'''
def func1(num):
    print(id(num))
    num = 10
    print(id(num))

temp = 20
print(id(temp))
func1(temp)   #num = temp
print(temp)   #输出20 

'''
引用传递：传递的可变类型
list、dict、set是可变的
'''
def func2(lis):
    lis[0] = 100
li = [1,2,3,4,5]
func2(li)  
print(li) #值可以改变



a = 10
b = 10
b = 40
print(id(a), id(b))

c = 20
d = 30
print(id(c), id(d))
d = c
print(id(c), id(d))

'''
值传递：传递的不可变类型
string、tuple、number是不可变的
'''
def func1(num):
    print(id(num))
    num = 10
    print(id(num))

temp = 20
print(id(temp))
func1(temp)   #num = temp
print(temp)   #输出20 

'''
引用传递：传递的可变类型
list、dict、set是可变的
'''
def func2(lis):
    lis[0] = 100
li = [1,2,3,4,5]
func2(li)  
print(li) #值可以改变

a = 10
b = 10
b = 40
print(id(a), id(b))

c = 20
d = 30
print(id(c), id(d))
d = c
print(id(c), id(d))

'''
概念：能处理比定义时更多的参数
'''

#关键字参数
'''
概念：允许函数调用时参数的顺序与定义时不一致

'''
def myPrint(str, age):
    print(str, age)

#使用关键字参数
myPrint(age = 18, str = "sunck is a good man")

#默认参数
'''
概念：调用函数时，如果没有传递参数，则使用默认参数
'''
#以要用默认参数，最好将默认参数放到最后
def myPrint(str, age = 18):
    print(str, age)

myPrint("kaige")


#不定长参数
#加了星号(*)的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组
def func(name, *args):
    print(name)
    print(type(args))
    for x in args:
        print(x)

func("sunck", "good", "nice", "handsom")

#求多个数的和
def mySum(*l):
    sum = 0
    for i in l:
        sum += i
    return sum
print(mySum(1,2,3,4,5,6,7))


#**代表简键值对的参数字典，和*所代表的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))

func2(x=1, y=2, z=3) #必须为关键字参数

#可以接受任意参数
def func3(*args, **kwargs):
    pass #代表一个空语句

#匿名函数
'''
概念：不使用def这样的语句定义函数，使用lambda来创建匿名函数

特点：
1、lambda只是一个表达式，函数体比def简单
2、lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3、lambda函数有自己的命名空间,且不能访问自由参数列表之外的或全局命名空间的参数
4、虽然lambda是一个表达式且看起来只能写一行，与C和C++内联函数不同。
   内联函数：减少程序的内存占用空间，提高程序的执行效率

格式：lambda 参数1,参数2,……,参数n:expression
'''

sum = lambda num1, num2:num1 + num2
print(sum(1,2))



