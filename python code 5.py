'''
tuple 元组

本质：是一种有序集合

特点：
1、与列表非常相似
2、一旦初始化就不能修改
3、使用小括号
'''
#创建tuple
#格式：元组名 = (元组元素1, 元组元素2, ……, 元组元素n)
#创建空的元组
tuple1 = ()
print(tuple1)
#创建带有元素的元组
#元组中的元素的类型可以不同
tuple2 = (1, 2, 3, "good", True)
print(tuple2)
#定义只有一个元素的元组
tuple3 = (1, )
print(tuple3)
print(type(tuple3))


 

#元组元素的访问
#格式：元组名[下标]
#下标从0开始
#取值
tuple4 = (1,2,3,4,5)
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3])
print(tuple4[4])
#print(tuple4[5]) #下标超过范围(越界)
#获取最后一个元素
print(tuple4[-1])  #获取最后一个元素
print(tuple4[-2])  #获取倒数第二个元素
print(tuple4[-5])
#print(tuple4[-6])#越界



#修改元组
tuple5 = (1,2,3,4,[5,6,7])
#tuple5[0] = 100  #报错，元组不能变
#tuple5[-1] = [7,8,9]
tuple5[-1][0] = 500
print(tuple5)



#删除元组
tuple6 = (1,2,3)
del tuple6
#print(tuple6)





#元组的操作
t7 = (1,2,3)
t8 = (4,5,6)
t9 = t7 + t8
#元组相加
print(t9)
print(t7, t8)

#元组重复 #元组相乘
t10 = (1,2,3)
print(t10 * 3)

#判断元素是否在元组中
t11 = (1,2,3)
print(4 in t11)  #返回true false

#元组的截取
#格式：元组名[开始下标:结束下标]
#从开始下标开始截取，截取到结束下标之前
t12 = (1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])



#二维元组:  元素为一维元组的元组
t13 = ((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])




#元组的方法

#len()   返回元组中元素的个数
t14 = (1,2,3,4,5)
print(len(t14))

#max()   返回元组中的最大值
#min()
print(max((5,6,7,8,9)))
print(min((5,6,7,8,9)))



#将列表转成元组
list = [1,2,3]
t15 = tuple(list)
print(t15)


#元组的遍历
for i in (1,2,3,4,5):
    print(i)


#字符串的处理
#split(str="", num)
#以str为分隔符截取字符串,指定num，则仅截取num个字符串
#num 默认等于str38.count()
str38 = "sunck**is******a***good*man"
#求单词个数
list39 = str38.split("*")
print(list39)
c = 0
for s in list39:
    if len(s) > 0:
        c += 1
print(c)

#按行处理切割
#splitlines([keepends])   按照('\r', '\r\n',  '\n')分隔
#keepends == True  会保留换行符  默认为False 不会保留换行符
str40 = '''sunck is a good man!
sunck is a nice man!
sunck is handsome man!
'''
print(str40.splitlines())


#join(seq)  以指定的字符串分隔符，将seq中的所有元素组合成一个字符串
list41 = ['sunck', 'is', 'a', 'good', 'man']
str42 = "&^%$#".join(list41)
print(str42)


#max()  min()
str43 = "sunck is a good man!z"
print(max(str43))
print("*"+min(str43)+"*")



#replace(oldstr, newstr, count)
#用newstr替换oldstr，默认是全部替换。如果指定了count，那么只替换前count个
str44 = "sunck is a good good good man"
str45 = str44.replace("good", "nice", 1)
print(str44)
print(str45)


#创建一个字符串映射表
print("************")
#                  要转换的字符串     目标字符串
t46 = str.maketrans("ac", "65")
#  a--6    c--5
str47 = "sunck is a good man"
str48 = str47.translate(t46)
print(str48)


#startswith(str, start=0, end=len(str)
#在给定的范围内判断是否是以给定的字符串开头，如果没有指定范围，默认整个字符串
str49 = "sunck is a good  man"
print(str49.startswith("sunck", 5, 16))

#endswith(str, start=0, end=len(str)
#在给定的范围内判断是否是以给定的字符串结尾，如果没有指定范围，默认整个字符串
str50 = "sunck is a nice man"
print(str50.endswith("man"))


#编码
#encode(encoding="utf-8", errors="strict")
str51 = "sunck is a good man凯"
#ignore忽略错误
data52 = str51.encode("utf-8", "ignore")
print(data52)
print(type(data52))

#解码  注意：要与编码时的编码格式一致
# 汉字会牵扯到编码解码的问题
str53 = data52.decode("gbk", "ignore")
print(str53)

#isalpha()  #不用传入任何树值
#如果字符串中至少有一个字符且所有的字符都是字母返回True,否则返回False
str54 = "sunckisagoodman"
print(str54.isalpha())

#isalnum()  不能有空格特殊编码符号 
#如果字符串中至少有一个字符且所有的字符都是字母或数字返回True,否则返回False
str55 = "1a2b3"
print(str55.isalnum())

#isupper()
#如果字符串中至少有一个英文字符且所有的英文字符都是大写的英文字母返回True,否则返回False
print("ABC".isupper())
print("1".isupper())
print("ABC1".isupper())
print("ABC#".isupper())

#islower()
#如果字符串中至少有一个英文字符且所有的英文字符都是小写的英文字母返回True,否则返回False
print("abc".islower())
print("abcA".islower())
print("1".islower())
print("abc1".islower())
print("abc#".islower())

#istitle()
#如果字符串是标题化的返回True，否则返回False 单词首字母大写
print("Sunck Is".istitle())
print("Sunck is".istitle())
print("sunck is".istitle())

#isdigit()
#如果字符串中只包含数字字符返回True，否则返回False
print("123".isdigit())
print("123a".isdigit())

#isnumeric()同上
print("123".isnumeric())
print("123a".isnumeric())

#isdecimal 字符串中只包含十进制字符
print("123".isdecimal())
print("123z".isdecimal())

#如果字符中只包含空格则返回True,否则返回False
print(" ".isspace())
print("      ".isspace())
print("\t".isspace())  #四个空格
print("\n".isspace())  #多个空格
print("\r".isspace())


'''
概述:
使用键-值(key-value)存储，具有极快的查找速度
key-value 键值对
注意：字典是无序的
value 数据类型不指定
key的特性：
1、字典中的key必须唯一
2、key必须是不可变对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能作为key
思考：保存多位学生的姓名与成绩
使用字典，学生姓名为key,学生成绩作为值

'''

dict1 = {"tom":60, "lilei":70}

#元素的访问
#获取：字典名[key]
print(dict1["lilei"])
#print(dict1["sunck"])#没有
print(dict1.get("sunck"))
ret = dict1.get("sunck")
if ret == None:
    print("没有")
else:
    print("有")


#添加  没有对应键是增加，有的就是修改
dict1["hanmeimei"] = 99
#因为一个key对应一个value,所以，多次对一个key的value赋值，其实就是修改值
dict1["lilei"] = 80

print(dict1)


#删除
#dict1.pop("tom")
#print(dict1)




#遍历
for key in dict1:
    print(key, dict1[key])

#print(dict1.values())
for value in dict1.values(): #[60,80,90]
    print(value)

#print(dict1.items())
for k, v in dict1.items():
    print(k, v)


for i, v2 in enumerate(dict1):
    print(i, v2)


#dict和list比较
#1、查找和插入的速度极快，不会随着key-value的增加而变慢
#2、需要占用大量的内存，内存浪费多



#list
#1、查找和插入的速度随着数据量的增多而减慢
#2、占用空间小，浪费内存少











