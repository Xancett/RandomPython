import random

def PlayGame():
    turns = 0
    number = random.randint(1, 101)
    while (turns < 5):
        guess = int(input("Enter a guess: "))
        if (guess > number):
            print("Too high")
        if (guess < number):
            print("Too low")
        if (guess == number):
            print("You win!")
            break
        turns += 1
    else:
        print("You lose! Number was ", number)

PlayGame()