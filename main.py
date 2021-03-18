import random

print("Welcome to my Adventure Game")
print("You are currently stuck in the ocean , 3000 miles below surface")
print("Your goal is reach the closeset submarine which is 20 miles away")
print("You got a cut on your leg so you're bleeding a lot. Hurry before the sharks sniff you out")

totalMilesSwam = 0
shark = -30 
bloodLeft = 80 
oxygenTank = 100 
oxygenSupply = 3 
bandages = 3 

print("A. Swim as fast as I can")
print("B. Switch oxygen tanks")

userInput = input("So what's your choice? ")

while(True):
  # Conditions to check for userInput
  if(userInput == "A"): 
    distanceSwam = random.randint(1,5)
    totalMilesSwam += distanceSwam 
    print("You swam " + distanceSwam)

    sharkSwam = random.randint(1,6)
    shark += sharkSwam

    bloodLeft -= 10
    oxygenTank -= 15
  elif(userInput == "B"): 
    if(oxygenSupply > 0): 
      oxygenTank = 100
      oxygenSupply -= 1 
      print("Great! Your tank has been switched")
    else: 
      print("Yikes sorry buddy... you're out of oxygen supply")

    sharkSwam = random.randint(1,6)
    shark += sharkSwam
  else: 
    print("Please choose a valid option")

  # Winning Condition(s)
  if(totalMilesSwam >= 20): 
    print("You win!")
    break
  
  # Losing Condition(s)
  if(shark >= totalMilesSwam): 
    print("You lose. The shark has eaten you up")
    break 

  # Warning Conditions 
  if(totalMilesSwam - shark <= 5): 
    print("The shark is getting dangerously close to you!")

  # Printing the options again and asking the user for another choice 
  print("A. Swim as fast as I can")
  print("B. Switch oxygen tanks") 
  userInput = input("So what's your choice?: ")