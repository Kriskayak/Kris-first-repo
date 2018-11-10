import turtle
#import sys
wn = turtle.Screen()
wn.bgcolor('purple')
size = wn.numinput('Size','How big would you like to go?')
#sys.getrecursionlimit()


t = turtle.Turtle()
t.color('blue')
t.pensize(1)
s = 0

while t.xcor() < size:
    t.right(89)
    t.forward (2 + s*2)
    s = s + 1
        
wn.exitonclick()
