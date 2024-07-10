from random import randint

guess = None
number = randint(1, 100)

def isEven():
  if (number % 2) == 0:
    print("Hint: number is Even!")
  else:
    print("Hint: number is NOT even!")

isEven()

while guess != number:
  guess = int(input("Guess a number up to 100!"))

  if guess > number:
    print("Your guess is too high!")
  if guess < number:
    print("Your guess is too low!")
  elif guess == number:
    print("You win!")
