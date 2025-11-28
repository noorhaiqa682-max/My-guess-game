import random

choice = 1      # We would want the loop to be executed at least once.
max_attempts = 3
score = 0       # Score will not discard until the user decides to leave or quit. We'll display it to the user when he quits.

while choice != 0:

    number = random.randint(1,10)
    guess = 0
    attempts = 0

    while attempts < max_attempts :

        guess = int(input("\nGuess a number (1-10): "))
        attempts +=1

        if guess < number:
            print("Too low! Attempts left: ", max_attempts - attempts)      # The left attempts would be maxAttempts - attempts, not max_attempts only
        elif guess > number:
            print("Too high! Attempts left: ", max_attempts - attempts)
        else:
            print("\nYou got it!")
            score += 10         # Score increments by 10 each time the user makes a right guess.
            break


        if attempts == max_attempts:
            print("\nOut of attempts! The number was", number)
            # print("Your score:",score)      # We would want to print the score when the user decides to quit.


    choice = int(input("\nWanna guess again? (0 to quit): "))

# The user has decided to quit.

# Print User progress.

# We could track different things. Like total number of attempts, number of times he played, number of times he won.

# Here we only have score. So, lets print that...

print("\nYou scored: ", score, " scores")
print("Visit again! 😃")