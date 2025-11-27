import random
number = random.randint(1,10)
guess = 0
attempts = 0
score = 0
max_attempts = 3
while attempts < max_attempts :
    guess = int(input("Guess a number (1-10): "))
    attempts +=1
    if guess < number:
        print("Too low! Attempts left:", max_attempts)
    elif guess > number:
        print("Too high! Attempts left:", max_attempts)
    else:
        print("You got it!")
        score = 10
        break
    if attempts==max_attempts:
        print("Out of attempts! The number was", number)
        print("Your score:",score)