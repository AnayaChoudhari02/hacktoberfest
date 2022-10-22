import random
num=random.randint(1,100)
print(num)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty =input("Choose a difficulty.Type 'easy' or 'hard'.")
count=10
end=False
if difficulty=='easy':
  print("You have 5 attempts remaining to guess the number.")
  
  while(count>0 and end==False):
    guess=int(input("Make a guess:"))
    if guess==num:
      print(f"You got it!The answer was {guess}")
      end=True
    elif guess<num and count!=1:
      print("Too low!")
      print("Guess again!")
      print(f"You have {count-1} attempts left.")
    elif guess>num and count!=1:
      print("Too high!")
      print("Guess again!")
      print(f"You have {count-1} attempts left.") 
    elif count==1:
      print("Sry,you lost!")
    count=count-1
    
count=5    
if difficulty=='hard':
  print("You have 5 attempts remaining to guess the number.")
  while(count>0 and end==False):
    guess=int(input("Make a guess:"))
    if guess==num:
      print(f"You got it!The answer was {guess}")
      end=True
    elif guess<num and count!=1:
      print("Too low!")
      print("Guess again!")
      print(f"You have {count-1} attempts left.")
    elif guess>num and count!=1:
      print("Too high!")
      print("Guess again!")
      print(f"You have {count-1} attempts left.") 
    elif count==1:
      print("Sry,you lost!")
    count=count-1
