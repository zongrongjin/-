import turtle

turtle.speed(1) #定义绘图速度
turtle.up()  #抬笔
#移动到起笔位置
turtle.backward(300)
turtle.left(90)
turtle.forward(230)
turtle.left(-90)  # 回归初始状态
#参数定义区
ro = 0  #定义行数
height = 0
angle = 90
Va = 19.8 #Vacuum acceleration 真空加速度
time = 0
Ga = 9.8
Ea = Va - Ga  #Effective acceleration  有效加速度
#基本IO模块
ro += 1 
turtle.write("%d. 火箭初始设定参数为：高度%d，对地角度为%d"%(ro,height,angle), font=("微软雅黑", 14, "normal"))
y = turtle.ycor()
x = turtle.xcor()
turtle.goto(x,y - 25)
ro += 1
turtle.write("%d. 火箭初始设定参数为：真空加速度%.1f，有效加速度为%.1f"%(ro,Va,Ea), font=("微软雅黑", 14, "normal"))
#基础换行模块
y = turtle.ycor()
x = turtle.xcor()
turtle.goto(x,y - 25)
ro += 1
turtle.write("%d. 基础设定为：初始时间%d s,重力加速度为%.1f m^2/s"%(ro,time,Ga), font=("微软雅黑", 14, "normal"))
#进阶IO模块
#格式调整
y = turtle.ycor()
x = turtle.xcor()
turtle.goto(x,y - 25)
ro += 1
turtle.write("%d. 火箭升空：时间%d s,实际加速度为%.1f m^2/s"%(ro,time,Ea), font=("微软雅黑", 14, "normal"))
y = turtle.ycor()
x = turtle.xcor()
turtle.goto(x,y - 25)
#格式调整完毕  IO进阶
while time < 9:
	ro += 1
	turtle.write("%d. 火箭升空：时间%.1f s,实际加速度为%.1f m^2/s"%(ro,time,Ea), font=("微软雅黑", 14, "normal"))
	y = turtle.ycor()
	x = turtle.xcor()
	turtle.goto(x,y - 25)
	ro += 1
	turtle.write("%d. 当前速度为%.1f m/s,实际加速度为%.1f m^2/s"%(ro,time*Ea,Ea), font=("微软雅黑", 14, "normal"))
	y = turtle.ycor()
	x = turtle.xcor()
	turtle.goto(x,y - 25)
	time += 0.5
	if ro == 20:
		break
turtle.done()  #使turtle不自动关闭


