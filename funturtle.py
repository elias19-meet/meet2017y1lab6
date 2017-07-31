import turtle
turtle.shape('turtle')
square = turtle.clone()
square.shape('square')
square.penup()



square.goto(100,100)
square.pendown()
square.forward(100)
square.left(90)
square.stamp()
square.forward(100)
square.left(90)
square.stamp()
square.forward(100)
square.left(90)
square.stamp()
square.forward(100)
tr=turtle.clone()
tr.shape('triangle')
tr.forward(100)
tr.stamp()
tr.left(120)
tr.forward(100)
tr.stamp()
tr.left(120)
tr.forward(100)
tr.stamp()
tr.left(120)
turtle.penup()
turtle.backward(200)
turtle.mainloop()





