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
    print("you moved up ")
    
def down():
    direction=DOWN
    print("you moved DOWN ")
    
def left():
    direction=LEFT
    print("you moverd left")
    
def right():
    direction=RIGHT
    print("you moved up ")
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
