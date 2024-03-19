from turtle import *
 
 
def nose(x, y):  # 鼻子
    penup()  # 提起笔
    goto(x, y)  # 定位
    pendown()  # 落笔，开始画
    setheading(-30)  # 将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    begin_fill()  # 准备开始填充图形
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            left(3)  # 向左转3度
            forward(a)  # 向前走a的步长
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()  # 填充完成
 
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255, 155, 192)  # 画笔颜色
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)  # 返回或设置pencolor和fillcolor
    end_fill()
 
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
 
 
def head(x, y):  # 头
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()
 
 
def cheek(x, y):  # 腮
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()
 
 
def mouth(x, y):  # 嘴
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)
 
 
def setting():  # 参数设置
    pensize(4)
    hideturtle()  # 使乌龟无形（隐藏）
    colormode(255)  # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(100)
 
 
def ears(x, y):
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()
 
 
def eyes(x, y):
    color((255, 155, 192), "pink")
    fillcolor('white')
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(0)
    circle(20)
    end_fill()
    color((255, 155, 192))
    fillcolor('white')
    penup()
    goto(x, y)
    begin_fill()
    forward(80)
    pendown()
    setheading(100)
    circle(20)
    end_fill()
    color('black')
    penup()
    goto(x-7, y+13)
    pendown()
    begin_fill()
    setheading(0)
    circle(5)
    end_fill()
    penup()
    goto(x, y)
    begin_fill()
    forward(60)
    pendown()
    setheading(100)
    circle(5)
    end_fill()
 
 
def body(x, y):
    width(5)
    color('firebrick')
    list = ['orangered', 'firebrick']
 
    up()
    goto(x, y)
    down()
    setheading(-105)
    begin_fill()
    fillcolor(list[0])
    circle(250, 30)
    setheading(0)
    forward(138)
    setheading(75)
    circle(250, 30)
    end_fill()
    setheading(-45)
    forward(70)
    begin_fill()
    fillcolor(list[1])
    circle(5)
    end_fill()
    up()
    goto(x, y)
    down()
    setheading(-145)
    forward(70)
    begin_fill()
    circle(5)
    end_fill()
    up()
    goto(x+20, y-250/2-4)
    down()
    setheading(270)
    forward(50)
    left(90)
    width(10)
    color('black')
    forward(13)
    width(5)
    color('firebrick')
    up()
    goto(x + 120, y - 250 / 2-4)
    down()
    setheading(270)
    forward(50)
    left(90)
    width(10)
    color('black')
    forward(13)
 
 
def main():
    body(-25, -15)
    setting()  # 画布、画笔设置
    nose(-100, 100)  # 鼻子
    head(-69, 167)  # 头
    ears(0, 160)  # 耳朵
    eyes(-15, 100)  # 眼睛
    cheek(80, 10)  # 腮
    mouth(-20, 30)  # 嘴
    done()
 
 
 
 
if __name__ == '__main__':
    main()