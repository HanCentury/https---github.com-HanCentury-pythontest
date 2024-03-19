'''
name:圣诞树+烟火
author:Babysen
'''
 
import turtle as t
import random
import threading
import time
import tkinter as tk
import math
from math import cos, sin, atan, sqrt
import numpy as np
 
t.screensize(bg='black')  # 定义背景颜色
 
# 心函数
def loving_heart(r):
    l = 2 * r
    t.left(45)
    t.forward(l)
    t.circle(r, 180)
    t.right(90)
    t.circle(r, 180)
    t.forward(l)
 
# 星函数
def loving_star(n):
    for i in range(5):
        t.forward(n / 5)
        t.right(144)
        t.forward(n / 5)
        t.left(72)
 
# 树函数(递归)
def tree(d, s):
    if d <= 0:
        return
    t.width(5)
    t.forward(s)
    tree(d - 1, s * .8)
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)  # 回退函数
 
 
# 画爱心部分
t.penup()
t.goto(0, 200)  # 设置起点位置
t.pendown()
t.pencolor('red')  # 设置画笔颜色
t.color('red')
t.begin_fill()  # 对图形进行填充
loving_heart(20)  # 执行画爱心函数
t.end_fill()
 
# 画树部分
n = 100
t.speed(0)
# t.Turtle().screen.delay(0)
t.right(225)
t.color("dark green")
t.backward(n * 4.8)
tree(15, n)
t.backward(n / 5)
 
# 绘制落叶
for i in range(100):
    a = 100 - 200 * random.random()
    b = 10 - 20 * random.random()
    t.speed(0)
    t.up()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.down()
    if random.randint(1, 2) == 1:
        t.color('tomato')
    else:
        t.color('wheat')
    t.circle(4)
    t.up()
    t.backward(a)
    t.right(90)
    t.backward(b)
 
# 绘制雪花
def drawsnow():  # 定义画雪花的方法
    t.speed(0)
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(2)  # 定义笔头大小
    for i in range(160):  # 画多少雪花
        t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        t.pu()  # 提笔，pu=penup
        t.setx(random.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        t.sety(random.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        t.pd()  # 落笔，pd=pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = random.randint(2, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            t.right(int(360 / dens))  # 转动角度
drawsnow()
 
# 画五角星
for i in range(-200,200,20):
    t.penup()
    t.goto(i, 300)  # 设置起点位置
    t.pendown()
    t.pencolor('yellow')  # 设置画笔颜色
    t.color('yellow')
    t.begin_fill()  # 对图形进行填充
    loving_star(30)
    t.end_fill()
    t.right(0)
 
for i in range(-150,150,20):
    t.penup()
    t.goto(i, 280)  # 设置起点位置
    t.pendown()
    t.pencolor('yellow')  # 设置画笔颜色
    t.color('yellow')
    t.begin_fill()  # 对图形进行填充
    loving_star(30)
    t.end_fill()
    t.right(0)
 
for i in range(-100,100,20):
    t.penup()
    t.goto(i, 260)  # 设置起点位置
    t.pendown()
    t.pencolor('yellow')  # 设置画笔颜色
    t.color('yellow')
    t.begin_fill()  # 对图形进行填充
    loving_star(30)
    t.end_fill()
    t.right(0)
 
for i in range(-50,50,20):
    t.penup()
    t.goto(i, 240)  # 设置起点位置
    t.pendown()
    t.pencolor('yellow')  # 设置画笔颜色
    t.color('yellow')
    t.begin_fill()  # 对图形进行填充
    loving_star(30)
    t.end_fill()
    t.right(0)
 
for i in range(-20,21,20):
    t.penup()
    t.goto(i, 220)  # 设置起点位置
    t.pendown()
    t.pencolor('yellow')  # 设置画笔颜色
    t.color('yellow')
    t.begin_fill()  # 对图形进行填充
    loving_star(30)
    t.end_fill()
    t.right(0)
 
# 写下署名
t.color("white")  # 填充颜色
t.up()  # 抬笔
t.goto(170, -240)
t.down()  # 落笔
t.write("Author:Babysen", font=("Times New Roman", 18, "normal"))
t.ht()
# t.done()
t.hideturtle()
time.sleep(2)
 
#烟火
WIDTH = 0
HEIGHT = 0
ORI = (0, 0)
COLOR = {'0': '#070920', 'navyblue': '#000080'}
FIRE = []
 
def setParam():
    global WIDTH
    global HEIGHT
    global ORI
    global FIRE
    WIDTH = t.window_width()
    HEIGHT = t.window_height()
    ORI = (0, -HEIGHT / 2)
    # gold
    FIRE.append(['white', '#FFD700', '#DAA520', '#BDB76B', ])
    # red
    FIRE.append(['white', '#F08080', '#A0522D', '#DC143C', ])
    # green
    FIRE.append(['white', '#7FFF00', '#32CD32', '#006400', ])
    # cyan
    FIRE.append(['white', '#40E0D0', '#00FFFF', '#008080', ])
    # pink
    FIRE.append(['white', '#FF69B4', '#FF1493', '#8B008B', ])
    # buff
    FIRE.append(['white', '#FFE4C4', '#FFDAB9', '#F0FFF0', ])
    # bluish
    FIRE.append(['white', '#ADD8E6', '#AFEEEE', '#00BFFF', ])
 
def dist(a, b):  # 距离
    return ((a - b) * (a - b)).sum()
 
def shoot():
    t.tracer(4)  # 在循环中，图形将一次画出4次循环的图
    t.pu()
    target = np.array((np.random.randint(-WIDTH // 6, WIDTH // 6),
                       HEIGHT // 6))  # 都在同一高度
    angle = atan((target - ORI)[1] / (target - ORI)[0])
    if angle < 0:
        angle += math.pi  # 纠正负方向
    unit = np.array([cos(angle), sin(angle)])  # 方向向量
    print('angle: ', angle)
    print('target: ', target)
    # 镜头的顺序坐标
    seq = np.array([ORI, ORI - 55 * unit, ORI - 105 * unit, ORI - 155 * unit])
    t.speed(0)  # 瞬动
    while dist(seq[0], target) > 120:  # 如果没有到达爆炸中心
        seq = seq + 30 * unit
 
        t.goto(seq[1])
        t.pd()
        t.width(3)
        t.pencolor('white')
        t.goto(seq[0])
        t.pu()
 
        t.goto(seq[2])
        t.pd()
        t.width(3)
        t.pencolor('yellow')
        t.goto(seq[1])
        t.pu()
 
        # 清除发射上去的光束尾迹
        t.goto(seq[3])
        t.pd()
        t.width(10)
        t.pencolor(COLOR['0'])
        t.goto(seq[2])
        t.pu()
        time.sleep(0.05)
 
    # 发射上去的光束最后清除
    t.pd()
    t.width(10)
    t.goto(seq[0])
    t.pu()
    time.sleep(0.1)
    return target  # 就在爆炸中心
 
def explode(center):
    number = np.random.randint(50, 100)  # 光束数
    colormode = np.random.randint(0, 5)
    unit = np.array([])  # 方向向量
    spd = []  # 每个光束的速度
    seq = []  # 每个波束的顺序坐标
    if colormode <= 1:
        coloridx = [np.random.randint(0, len(FIRE))]
    elif colormode == 2:
        coloridx = [np.random.randint(0, len(FIRE)),
                    np.random.randint(0, len(FIRE))]
    elif colormode == 3:
        coloridx = [np.random.randint(0, len(FIRE)),
                    np.random.randint(0, len(FIRE)),
                    np.random.randint(0, len(FIRE))]
    elif colormode == 4: 
        coloridx = []
 
    # 不同大小烟花的步骤
    steps = int((number ** 0.5) * 2)
 
    # 初始化
    for i in range(number):
        angle = np.random.rand() * 2 * math.pi - math.pi
        unit = np.append(unit, [cos(angle), sin(angle)]).reshape(-1, 2)
        seq = np.append(
            seq,
            [center,
             center - 10 * unit[i], center - 50 * unit[i],
             center - 90 * unit[i], center - 130 * unit[i],
             center - 135 * unit[i]]
        )
        spd.append(int(15 + (np.random.rand() - 0.5) * 5))
 
        if colormode <= 1:
            coloridx.append(coloridx[0])
        elif colormode == 2:
            coloridx.append(coloridx[np.random.randint(0, 2)])
        elif colormode == 3:
            coloridx.append(coloridx[np.random.randint(0, 3)])
        elif colormode == 4:
            coloridx.append(np.random.randint(0, len(FIRE)))
 
    seq = seq.reshape([-1, 6, 2]).astype(np.int32)
    t.tracer(0x3f3f3f3f)  # 关闭自动更新，0x3f3f3f3f是一个大数字 
 
    for stage in range(steps):
        for i in range(number):
            seq[i] = seq[i] + spd[i] * unit[i]
            seq[i][4] = center
            for cur in range(4):
                t.pu()
                t.goto(seq[i][cur + 1])
                t.pd()
                t.pencolor(FIRE[coloridx[i]][cur])
                t.width(4 - cur)
                t.goto(seq[i][cur])
                t.pu()
        if stage >= 5:  # 等待所有光束就位
            t.update()
            time.sleep(0.04)
 
    # 清除每次绽放的烟花
    for cur in range(4, -1, -1):
        for i in range(number):
            t.pu()
            t.goto(seq[i][cur + 1])
            t.pd()
            t.pencolor(COLOR['0'])
            t.width(100)
            t.goto(seq[i][cur])
            t.pu()
        time.sleep(0.02)
        t.update()
 
def main():
    t.setup(700, 750, 100, 0)
    setParam()
    while True:
        point = shoot()
        explode(point)
    exitonclick()  # 在任何位置单击退出
 
if __name__ == '__main__':
    main()