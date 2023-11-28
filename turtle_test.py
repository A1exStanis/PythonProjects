import turtle as t

t.speed(1)

def drawSqure(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)

drawSqure(100)

t.goto(200,300)

drawSqure(50)