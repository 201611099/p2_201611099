import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

t2=turtle.Turtle()
t2.penup()
t2.setpos(100,200)
t2.pendown()
t2.forward(200)

def keyup():
         t1.forward(50)

def keydown():
         t1.back(50)


def keyleft():
         t1.left(90)

def keyright():
         t1.right(90)

def mousegoto(x,y):
     t1.setpos(x,y)
     t1.pos=(x,y)
     if 100<=x<=300 and 200<=y<=200:
          print "Correct"
def addKeys():
     wn.onkey(keyup,"Up")
     wn.onkey(keydown,"Down")
     wn.onkey(keyleft,"Left")
     wn.onkey(keyright,"Right")

def addMouse():
     wn.onclick(mousegoto)

addKeys()
addMouse()

wn.listen()
turtle.mainloop()


