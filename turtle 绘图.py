import turtle

turtle.setup(width=1.0,height=1.0) #设置绘图区域大小

turtle.speed(10) #绘图速度
turtle.up() #抬笔
turtle.goto(-650,-300)  #移动到原点
turtle.down()  #落笔
#绘制X轴
turtle.forward(1300)   #X轴长度1300
#	绘制X坐标箭头
turtle.begin_fill()
turtle.fillcolor("black")
turtle.goto(645,-300)
turtle.goto(643,-296)
turtle.goto(650,-300)
turtle.goto(643,-304)
turtle.goto(645,-300)
turtle.end_fill()
#抬笔回原点
turtle.up()
turtle.goto(-650,-300)
turtle.left(90)
for x in range(-650,650,100):
	turtle.goto(x,-300)
	turtle.down()
	turtle.forward(10)
	turtle.up()
	turtle.backward(30)
	turtle.write("%d"%(x + 650))
#	Y轴坐标分度绘制完成
turtle.right(90)
#X轴绘制完成	

turtle.up() #抬笔
turtle.goto(-650,-300)  #移动到原点
turtle.down() 
turtle.left(90)
turtle.goto(-650,350)   #Y轴长度600

#	绘制Y坐标箭头
turtle.begin_fill()
turtle.fillcolor("black")
turtle.goto(-650,355)
turtle.goto(-654,353)
turtle.goto(-650,360)
turtle.goto(-646,353)
turtle.goto(-650,355)
turtle.end_fill()
#	箭头绘制结束
turtle.up() #抬笔
turtle.right(90)
#	绘制Y轴坐标分度
for y in range(-300,400,100):
	turtle.goto(-650,y)
	turtle.down()
	turtle.forward(10)
	turtle.up()
	turtle.backward(35)
	turtle.write("%d"%(y + 300))

#	Y轴坐标分度绘制完成
#坐标系绘制完成

#绘图 
turtle.speed(1)
turtle.up() #抬笔
turtle.goto(-650,-300)  #移动到原点
turtle.down()  #落笔
turtle.speed(1)   
turtle.left(90)    
turtle.forward(45)
turtle.right(5)  #5
turtle.forward(65)
turtle.right(5)  #10
turtle.forward(55)
turtle.right(5)  #15
turtle.forward(65)
turtle.right(5)  #20
turtle.forward(55)
turtle.right(5)  #25
turtle.forward(65)
turtle.right(5)  #30
turtle.forward(65)
turtle.right(5)  #35
turtle.forward(75)
turtle.right(5)  #40
turtle.forward(85)
turtle.right(5)  #45
turtle.forward(95)
turtle.done()