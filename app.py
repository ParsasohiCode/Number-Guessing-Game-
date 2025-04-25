import random
print("Welcome to the Number Guessing Game!")
print("-"*30)
print("I'm thinking of a number between 1 and 100.")
print("selecet your difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard") 
level = int(input("Enter your choice: "))
print("*"*30)
if level == 1:
    attempts = 10
elif level == 2:
    attempts = 5
elif level == 3:
    attempts = 3
else:
        print("Invalid choice. Please try again.")
        exit()
number = random.randint(1, 100)
i = 1
while i <= attempts:
  try:
    guess = int(input(f"attempt number {i} Make a guess: "))
    if guess == number:
        print(f"Congratulations! You guessed the number in {i+1} attempts.")
        break
    elif guess < number:
        print("Too low. Try again.")
        print("-"*30)
        i+=1
    else:
        print("Too high. Try again.")
        print("-"*30)
        i+=1
  except ValueError:
    print("Invalid input. Please enter a valid number.")
    
if i > attempts:
    print(f"Sorry, you've run out of attempts. The number was {number}.")
    print("*"*30)