# Name: Dia Yamamoto 
# Purpose: this program will produce star art in the console 

# rectangle made of stars
for i in range(8):
  for j in range(8):
    print("*", end = "")
  print()

# triangle made of stars
for i in range(8):
  for j in range(i+1):
    print("*", end = "")
  print()

# upside down triangle of stars
for row in range(8):
  for column in range(8-row):
    print("*", end = "")
  print()

# equilateral triangles
for j in range(8):
  for i in range(7-j):
    print(" ", end = "")
  for k in range(j):
    print("**", end = "")
  print("*")

# upside down equilateral triangle
for j in range(8):
  for i in range(j):
    print(" ", end = "")
  for k in range(7-j):
    print("**", end = "")
  print("*")


# import turtle library
import turtle

#create a turtle named fluffy
fluffy = turtle.Turtle()
# turtle shapes: circle, square, triangle, arrow, classic, or turtle
fluffy.shape("turtle")
# fluffy is going to be green
fluffy.color("green")

#for loop to design circular hexagon
for i in range(50):
  fluffy.right(100)
  fluffy.forward(70 + i)
  fluffy.left(40)
