import turtle
import math
import time

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def shiftcolors(myList):
    if len(myList) > 0:
        color = myList[0]
        myList.pop(0)
        myList.append(color)
    return myList
        
    
turtle.bgcolor('black')
colors = ['yellow', 'green', 'blue','purple','red','orange']

bobRoss = turtle.Turtle()
bobRoss.speed(1000000)
sLen = 1
bobRoss.pensize(1)
for i in range(0,720):
    bobRoss.pencolor(colors[i%6])
    polygon(bobRoss, 3, sLen)
    bobRoss.forward(i)
    bobRoss.left(59)
    sLen+=1

