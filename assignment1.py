import turtle

# init
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(5)

# head
def draw_circle(radius, color, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# eyes
def draw_eye(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.dot(30, "white") 
    pen.dot(15, "black")  

# nose
def draw_nose():
    pen.penup()
    pen.goto(-10, 0)
    pen.pendown()
    pen.fillcolor("pink")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(20)
        pen.left(120)
    pen.end_fill()

# mouth
def draw_mouth():
    pen.penup()
    pen.goto(-20, -10)
    pen.setheading(-90)
    pen.pendown()
    pen.circle(10, 180)  
    pen.penup()
    pen.goto(0, -10)
    pen.setheading(-90)
    pen.pendown()
    pen.circle(10, 180)  

# whiskers
def draw_whiskers():
    for y_offset in [-10, -15, -5]:
        pen.penup()
        pen.goto(-100, y_offset)
        pen.setheading(0)
        pen.pendown()
        pen.forward(60)

    for y_offset in [-10, -15, -5]:
        pen.penup()
        pen.goto(100, y_offset)
        pen.setheading(180)
        pen.pendown()
        pen.forward(60)

# ears
def draw_ears():
    draw_circle(30, "gray", -70, 80)  
    draw_circle(15, "pink", -70, 95)  
    draw_circle(30, "gray", 70, 80)   
    draw_circle(15, "pink", 70, 95)   


draw_circle(100, "gray", 0, -50) 
draw_ears()  
draw_eye(-40, 40)  
draw_eye(40, 40)   
draw_nose()  
draw_mouth()  
draw_whiskers()

# finish
pen.hideturtle()
screen.mainloop()
