# Name: Dia Yamamoto
# This program will draw different shapes using Turtle

import turtle 

# creation of a turtle
edward = turtle.Turtle() 
edward.shape("turtle")
edward.speed(1)

#turtle drawing a square 
for i in range(4):
  edward.forward(50)
  edward.left(90)

edward.clear()
edward.home()

#turtle drawing a house 
for i in range(5):
  edward.left(90)
  edward.forward(50)

edward.left(45)
edward.forward(40)
edward.left(90)
edward.forward(40)

edward.clear()
edward.penup()
edward.home()

#turtle drawing star
edward.pendown()
for i in range(5):
  edward.forward(80)
  edward.right(144)

edward.clear()
edward.home()

# turtle drawing flower
# circle
for i in range(60):
  edward.forward(2)
  edward.left(6)
edward.pu()

# petals
edward.forward(19)
edward.pd()
for i in range(4):
  edward.forward(5.3)
  for j in range(30):
    edward.forward(2)
    edward.left(6)
  edward.forward(5.3)
  edward.right(90)
  
# stem 
edward.right(80)
for i in range(10):
  edward.right(1)
  edward.forward(8)

