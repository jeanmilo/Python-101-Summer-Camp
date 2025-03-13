# Name: Dia Yamamoto
# Purpose: this is a tic tac toe game built using turtle

import turtle

def draw_grid(tom, size):
  # vertical left line
  tom.penup()
  tom.goto(-size/2, -size*1.5)
  tom.pendown()
  tom.goto(-size/2, size*1.5)

  # vertical right line
  tom.penup()
  tom.goto(size/2, -size*1.5)
  tom.pendown()
  tom.goto(size/2, size*1.5)

  # horizontal top line
  tom.penup()
  tom.goto(size*1.5, size/2)
  tom.pendown()
  tom.goto(-size*1.5, size/2)

  # horizontal bottom line
  tom.penup()
  tom.goto(-size*1.5, -size/2)
  tom.pendown()
  tom.goto(size*1.5, -size/2)

def draw_char(tom, size, cell, char):
  #register all posible x & y coordinate placements 
  x_coor = [-size, 0, size, -size, 0, size, -size, 0, size] 
  y_coor = [size, size, size, 0, 0, 0, -size, -size, -size]
  x = x_coor[cell]
  y = y_coor[cell]

  # put char at the designated coordinate 
  tom.penup()
  tom.goto(x, y)
  tom.write(char, False, "center", "32pt")

def test_winner(assigned, char):
  test = [0,1,2, 3,4,5, 6,7,8,  0,3,6,  1,4,7,  2,5,8,  0,4,8,  2,4,6]
  for i in range(8): 
    tests = []
    for j in range(3):
      tests.append(assigned[test[(i*3)+j]])
    if tests == [char, char, char]:
      return True
  return False


# main code
size = 50
megatron = turtle.Turtle()
draw_grid(megatron, size)
chars = ["X", "O"]

#check if cell has already been assigned
assigned = [0, 0, 0, 0, 0, 0, 0, 0, 0] 

for i in range(9):
  char = chars[i % 2] #do not worry abt this
  cell = int(input("Enter a cell number to put a " + char + ": "))
  cell -= 1 #do not worry abt this 

  # check if valid number
  if cell > -1 and cell < 9:
    # check if number already used
    if assigned[cell] == 0: 
      assigned[cell] = char
      draw_char(megatron, size, cell, char)
      if test_winner(assigned, char):
        print(char + " is the winner!")
        break
    else: 
      print("That cell already has a character, you lose a turn.")
  else:
    print("That is an invalid number, you lose a turn")


  


