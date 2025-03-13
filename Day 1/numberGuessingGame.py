# Name: Dia Yamamoto 
# Purpose: this program is a number guessing game 

import random 

# picks random number out of 100
randomNumber = random.randint(1,100)

# count number of guesses
guessCount = 1

#forever loop
while True: 
  #get players guess
  guess = int(input("Type in a number from 1 - 100: "))
  
  #check if guess is correct
  if guess == randomNumber:
    print("You got it!!")
    print("It took you "+str(guessCount)+" tries to get it right")
    break 
    
  # check if guess is larger than our answer
  elif guess > randomNumber:
    print("That's too high, try guessing lower")
    # add 1 to guess count to try again
    guessCount = guessCount + 1
    
  # check if guess is smaller than our answer
  elif guess < randomNumber: 
    print("That's too low, try guessing higher")
    # add 1 to guessCount to try again
    guessCount = guessCount + 1

