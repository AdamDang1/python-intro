import random

number = random.randint(1, 100)
player_name = input("Greetings, Earthling. What is your name?\n")
print("Okay " + player_name + ", I'm thinking of a number between 1 and 100.\n" "Try to guess my number.")
number_of_tries = 0

while number_of_tries < 100:
    guess = int(input("Your guess?\n"))
    number_of_tries += 1
    if guess < number:
        print("Your guess is too low, try again.")
    elif guess > number:
        print("Your guess is too high, try again.")
    else:
        print("Well done, " + player_name + "! You found my number in " + str(number_of_tries) + " tries!")