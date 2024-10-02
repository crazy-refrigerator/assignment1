from turtle import *

def draw_crayonshinchan():
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

    penup()  
    pensize(10)
    goto(-60, 0) 
    color("black")
    left(90)
    pendown()  
    length = 20
    forward(length) 
    left(90)
    length = 20
    forward(length) 

    penup() 
    pensize(10)
    goto(5, -5)  
    color("black")
    right(90)
    pendown()  
    length = 20
    forward(length)  
    left(90)
    length = 20
    forward(length)

    #ear
    penup()
    goto(50, -60)  
    setheading(0) 
    pendown()
    color("black") 
    circle(15, 180) 

    hideturtle()


draw_crayonshinchan()

exitonclick()
