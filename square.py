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
    s = s + 4

wn.exitonclick()

#this is the second branch comment 900
#this is another second branch comment 913

#this is another master comment 1116
#this is a second branch edit   912

#master edit 1146
