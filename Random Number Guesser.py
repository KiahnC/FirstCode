import random

lownum = int(input("Enter lowest number: "))
highnum = int(input("Enter highest number: "))

randomnum = random.randint(lownum, highnum)
guessed = False

print(" ")
print("Random number has been generated!")
print(" ")

while guessed == False:
    guess = int(input("Guess a number: "))
    if guess < randomnum:
        print("Too Low!")
    if guess > randomnum:
        print("Too High!")
    if guess == randomnum:
        print("You guessed the correct number! Good job!")
        pa = input("Play again? y/n ")
        if pa == "y":
            continue
        if pa == "n":
            break

