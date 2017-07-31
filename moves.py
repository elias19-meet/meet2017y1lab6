import turtle
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP
def up():
    direction=UP
    
    turtle.forward(50)
    print("you moved up ")
    
def down():
    direction=DOWN
    turtle.backward(50)
 
    print("you moved DOWN ")
    
def left():
    direction=LEFT
    turtle.left(90)
    
    print("you moverd LEFT")
    
def right():
    direction=RIGHT
    turtle.right(90)
    
    print("you moved right ")

turtle.onkeypress(turtle.stamp,SPACEBAR)
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()
