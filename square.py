import turtle
#import sys
wn = turtle.Screen()
wn.bgcolor('green')
size = wn.numinput('Size','How big would you like to go?')

t = turtle.Turtle()
t.color('silver')
t.pensize(1)
s = 0

while t.xcor() < size:
    t.right(89)
    t.forward (2 + s*2)
    s = s + 3

wn.exitonclick()
#this is a test comment

#this is a first branch comment 1127

