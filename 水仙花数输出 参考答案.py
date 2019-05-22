#练习参考答案  水仙花数输出
num = 100
while num  <= 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100

    if num == a**3 + b**3 + c**3:
        print(num)
    num += 1
