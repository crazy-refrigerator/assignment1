from turtle import *

def draw_crayonshinchan():
    # 设置画笔速度
    speed(6)

    penup()
    goto(0, -100)
    setheading(45)
    pendown()
    begin_fill()
    color("peachpuff")
    for _ in range(2):
        circle(50, 90)
        circle(100, 90)
    end_fill()
    penup()

    goto(50,-100)
    pendown()
    begin_fill()
    circle(100)
    end_fill()

    penup()
    goto(-100,-100)
    pensize(5)
    begin_fill()
    color("pink")
    circle(10)
    end_fill()

    penup()
    pensize(5)
    goto(-55,-50)
    begin_fill()
    color("black")
    circle(20)
    end_fill()

    penup()
    pensize(5)
    goto(-60, -45)
    begin_fill()
    color("white")
    circle(10)
    end_fill()

    penup()
    pensize(5)
    goto(5, -55)
    begin_fill()
    color("black")
    circle(20)
    end_fill()

    penup()
    pensize(5)
    goto(0, -50)
    begin_fill()
    color("white")
    circle(10)
    end_fill()

    penup()  # 抬起画笔
    pensize(10)
    goto(-60, 0)  # 移动到起点
    color("black")
    left(90)
    pendown()  # 落下画笔
    length = 20
    forward(length)  # 绘制长度为 length 的线段
    left(90)
    length = 20
    forward(length)  # 绘制长度为 length 的线段

    penup()  # 抬起画笔
    pensize(10)
    goto(5, -5)  # 移动到起点
    color("black")
    right(90)
    pendown()  # 落下画笔
    length = 20
    forward(length)  # 绘制长度为 length 的线段
    left(90)
    length = 20
    forward(length)  # 绘制长度为 length 的线段

    #ear
    penup()
    goto(50, -60)  # 移动到右下方位置
    setheading(0)  # 朝右侧
    pendown()
    color("black")  # 选择半圆的颜色
    circle(15, 180)  # 半径为 100，绘制 180 度的弧

    # 完成
    hideturtle()


# 调用绘制函数
draw_crayonshinchan()

# 点击窗口时退出
exitonclick()
