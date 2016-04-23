import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

t1.penup()
t1.setpos((-400,120))
t1.pendown()
t1.pencolor("GREEN")

def drawTriangleAt(size,pos):
    t1.fd(size)
    t1.setheading(120)
    t1.fd(size)
    t1.setheading(240)
    t1.fd(size)

size=100
drawTriangleAt(size,(-400,120))

t1.penup()
t1.setpos((-250,-200))
t1.pendown()
t1.pencolor("ORANGE")

def drawCircleAt(size,pos):
    t1.circle(size)

size=70
drawCircleAt(size,(-250,-200))

t1.penup()
t1.setpos((250,180))
t1.pendown()
t1.setheading(0)
t1.pencolor("PURPLE")

def drawPolygonAt(size,pos):
    t1.fd(size)
    t1.setheading(60)
    t1.fd(size)
    t1.setheading(120)
    t1.fd(size)
    t1.setheading(180)
    t1.fd(size)
    t1.setheading(240)
    t1.fd(size)
    t1.setheading(300)
    t1.fd(size)
    
size=80
drawPolygonAt(size,(250,180))

t1.penup()
t1.setpos((-70,350))
t1.pendown()
t1.pencolor("BLUE")

def drawRectangleAt(size,pos):
    t1.fd(size)
    t1.right(90)
    t1.fd(size)
    t1.right(90)
    t1.fd(size)
    t1.right(90)
    t1.fd(size)
    
    
size=120
drawRectangleAt(size,(-70,350))

t1.penup()
t1.setpos((280,-100))
t1.pendown()
t1.setheading(0)
t1.pencolor("RED")

def drawStarAt(size,pos):
    t1.setheading(144)
    t1.fd(size*3/8)
    t1.penup()
    t1.fd(size/4)
    t1.pendown()
    t1.fd(size*3/8)
    t1.setheading(288)
    t1.fd(size*3/8)
    t1.penup()
    t1.fd(size/4)
    t1.pendown()
    t1.fd(size*3/8)
    t1.setheading(72)
    t1.fd(size*3/8)
    t1.penup()
    t1.fd(size/4)
    t1.pendown()
    t1.fd(size*3/8)
    t1.setheading(216)
    t1.fd(size*3/8)
    t1.penup()
    t1.fd(size/4)
    t1.pendown()
    t1.fd(size*3/8)
    t1.setheading(0)
    t1.fd(size*3/8)
    t1.penup()
    t1.fd(size/4)
    t1.pendown()
    t1.fd(size*3/8)
    
size=200
drawStarAt(size,(280,-100))

t1.penup()
t1.setpos((0,0))
t1.pendown()
t1.shape("turtle")
t1.pencolor("BLACK")