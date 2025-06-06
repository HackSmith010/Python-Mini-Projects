import random

guess = int(input("Guess a number between 1 and 100: "))
number = random.randint(1, 100)
count = 0
while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess again: "))
    
    count = count+1

print("You got it!")
print(f"You took {count} tries")