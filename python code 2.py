﻿'''
#什么是字符串

字符串是以单引号或双引号括起来的任意文本
'abc'
"def"  #字符串为括号内的文本
字符串不可变
#创建文本串
#创建字符串
#定义字符串的变量
'''
str1 = "sunck is a good man!"

#字符串的运算
#1.字符串的连接
str6 = "sunck is a "
str7 = "good man"
str8 = str6 + str7
print("str6 =", str6)
print("str7 =", str7)
print("str8 =", str8)

#输出重复字符串
str9 = "good"
str10 = str9 * 3
print("str10 =", str10)

#访问字符串中的某一个字符
#通过索引下标查找字符，索引从0开始
#字符串名[下标]
str11 = "sunck is a good man!凯"
print(str11[1])
#str11[1] = "a" #字符串不可变
#中文根据编码占据2~4个字节。 与笔划数相关
#索引与字符相关  
#空格也是一个字符
print("str11 =", str11)

#截取字符串中的一部分
str13 = "sunck is a good man!"
#从给定下标出开始截取到给定下标之前
str15 = str13[6:15]
#从头截取到给定下标之前
str16 = str13[:5]
#从给定下标处开始截取到结尾  #超了也不影响结果
str17 = str13[16:]
print("str17 =", str17)

#判断单词是否在字符串之间
str18 = "sunck is a good man"
print("good" in str18)
print("good1" not in str18)

#print(~5) #取反

#格式化输出
print("sunc is a good man")
num = 10
str19 = "sunck is a nice man!"
f = 10.1267
print("num =", num, "str19 =", str19)
#  %d   %s   %f  占位符
#                                   精确到小数点后3位，会四舍五入
print("num = %d, str19 = %s, f = %.3f" % (num, str19, f))

#转义字符  \
#将一些字符转换成有特殊含义的字符

#\n 换行
print("num = %d\nstr19 = %s\nf = %.3f" % (num, str19, f))

#\ 增加斜杠 
print("sunck \\ is")

# \'   \"
print('tom is a \'good\' man')
print("tom is a \"good\" man")
#单引号和双引号交叉使用
print("tom is a 'good' man")
#      tom is a 'good' man

#如果字符串内有很多换行，用\n写在一行不好阅读
print("good\nnice\nhandsome")
print('''
good
nice
handsome
''')  #多行打印输出 直观

#\t   制表符   Windows默认四个空格 Linus默认八个空格
print("sunck\tgood")

#如果字符中有好多字符串都需要转义，就需要加入好多\，为了简化，Python允许用r表示内部的字符串默认不转义
#     \\\t\\
print(r"\\\t\\")
print(r"C:\Users\xlg\Desktop\Python-1704\day03")
print("C:\\Users\\xlg\\Desktop\\Python-1704\\day03")

#不同路径的表示方法
#windows
#  C:\\Users\\xlg\\Desktop\\Python-1704\\day03
#linux
#  /root/user/sunck/Desktop/Python-1704/day03



#数据处理即处理字符串
#字符串批量处理的方法

#eval(str)  可以传入三个参数  str代表字符串
#功能：将字符串str当成有效的表达式来求值并返回计算结果
num1 = eval("123")
print(num1)
print(type(num1))
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))
#print(eval("a123"))
#print(eval("12a3"))

#len(str)
#返回字符串的长度(字符个数)
print(len("sunck is a good man凯"))

#lower()转换字符串中大写字母为小写字母
str20 = "SUNCK is a Good Man!凯"
str21 = str20.lower()
print(str21)
print("str20 = %s" %(str20))
#中文 符号不影响 
#upper()转换字符串中小写字母为大写字母
str21 = "SUNCK is a Good Man!"
print(str21.upper())

#swapcase()转换字符串中小写字母为大写字母,大写字母为小写字母
str22 = "SUNCK is a gOOd mAn!"
print(str22.swapcase())
#capitalize()  首字母大写，其他小写
str23 = "SUNCK is a gOOd mAn!"
print(str23.capitalize())
#title()每个单的首字母大写
str24 = "SUNCK is a gOOd mAn!"
print(str24.title())
#  character   char #字符类型
#center(width[, fillchar]) 宽度 填充字符
#返回一个指定宽度的居中字符串，fillchar为填充的字符串,默认空格填充  居中填充
str25 = "kaige is a nice man"
print(str25.center(40,"*"))
#ljust(width[, fillchar]) 
#返回一个指定宽度的左对齐字符串，fllchar为填充字符，默认空格填充  左对齐填充
str26 = "kaige is a nice man"
print(str26.ljust(40, "%"))
#rjust(width[, fillchar])
#返回一个指定宽度的右对齐字符串，fllchar为填充字符，默认空格填充
str27 = "kaige is a nice man"
print(str26.rjust(40, "%"))

#zfill(width)  zerofill
#返回一个长度为width的字符串，原字符串右对齐，前面补0
str28 = "kaige is a nice man"
print(str28.zfill(40))

#count(str[,start][,end])
#返回字符串中strc出现的次数，可以指定一个范围，默认从头到尾
str29 = "kaige is a very very nice man"
print(str29.count("very"))
print(str29.count("very",15, len(str29) ))

#find(str[, start][,end])
#从左向右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾。得到的是第一次出现的开始下标，没有返回-1
str30 = "kaige is a very very nice man"
print(str30.find("very"))
print(str30.find("good"))  
print(str30.find("very", 15, len(str30))) #从15处去找very的位置，返回字符串的位置

#rfind(str[, start][,end])] #从右至左
str30 = "kaige is a very very nice man"
print(str30.rfind("very"))
#print(str30.rfind("good"))
print(str30.rfind("very", 0, 15))

#index(str, start=0, end=len(str))
#跟find()一样，只不过如果str不存在的时候回报一个异常
str31 = "kaige is a very very nice man"
#print(str31.index("good"))

#rindex(str, start=0, end=len(str))
#根rfind()一样，只不过如果str不存在的时候回报一个异常
str32 = "kaige is a very very nice man"
#print(str32[0:12])
print(str32.rindex("very"))


#lstrip()截掉字符串左侧指定的字符，默认为空格
str33 = "*******kaige is a nice man"
print(str33.lstrip("*"))

#rstrip()截掉字符串右侧指定的字符，默认为空格
str34 = "kaige is a nice man          "
print(str34.rstrip(), "*")

#strip()截取字符串内部指定的字符，默认为空格
str35 = "*******kaige is a nice man*********"
print(str35.strip("*"))
























