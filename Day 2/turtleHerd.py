# Name: Dia Yamamoto
# Purpose: create a herd of turtles!! with the help of a new tool we'll learn called: functions!! 

# cant have a turtle game without inviting turtle first!
import turtle

# Create a welcome message function
def welcomeMessage():
  print()
  print("Welcome to our herd of turtles demo.")
  print()

# get a number from the player using input()
def getInput(): 
  num = eval(input("Please enter the number of turtles: "))
  return(num)

# create/set up our background screen
def setUpScreen(): 
  w = turtle.Screen()
  w.bgcolor("green")
  return w 

# now we will create our turtles
def setUpTurtles(num): 
  # we need a list to keep track of all the turtles we'll create
  tList = []  #create a list for our turtles
  
  # create turtles
  for i in range(num):
    t = turtle.Turtle() # create turtle 
    t.shape("turtle")   # make turtle turtle-shaped 
    tList.append(t)     # add turtle to list

  for i in range(num):
    tList[i].color(0, 0, i / (2 * num) + .5) # this code is a bit ugly D: we will  
    tList[i].right(i * 360 / num)            # go over the math on the whiteboard

  return tList # lets use our list to tell our turtles where they will move to 

# let's make our turtles move!
def moveForward(tList):
  for t in tList:
    t.forward(30)

# lets stamp our turtles in our game! 
def stamp(tList):
  for t in tList:
    t.stamp()

# create our last function which will now tell our code to do all the functions we created!
def main():
  welcomeMessage()
  numTurtles = getInput()
  w = setUpScreen()
  turtleList = setUpTurtles(numTurtles)
  for i in range(10):
    moveForward(turtleList)
    stamp(turtleList)

if __name__ == "__main__":
  main()

