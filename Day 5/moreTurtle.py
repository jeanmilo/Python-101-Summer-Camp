# Name: Dia Yammaoto
# Purpose: This program will investigate the turtle world and its possibilities

import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
harry = turtle.Turtle()
harry.shape("turtle")

def draw_house(turtle, color, size, x, y):
  turtle.penup()
  turtle.color("black") # outline of house
  turtle.fillcolor(color) # color of house
  turtle.goto(x,y) # lower left corner
  turtle.pendown()
  turtle.begin_fill()
  turtle.goto(x, y+size) # top left corner
  turtle.goto(x+size, y) # diagonal right corner
  turtle.goto(x,y) # back to lower left
  turtle.goto(x+size, y+size) #diagonal top right
  turtle.goto(x, y+size) #top left
  turtle.goto(x+size/2, y+size*1.5) # roof
  turtle.goto(x+size, y+size) #upper right corner
  turtle.goto(x+size, y) #bottom right corner
  turtle.end_fill()

def draw_star(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.goto(x,y)
  turtle.pendown()
  for i in range(5):
    turtle.forward(size)
    turtle.right(144)
  turtle.end_fill()

#for i in range(10):
while True:
  x = random.randint(-200,200)
  y = random.randint(-200, 200)
  size = random.randint(10,100)
  color = random.choice(colors)
  #draw_house(harry, color, size, x, y)
  draw_star(harry, color, size, x, y)
