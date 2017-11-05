import random

def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # get a number guess from the player
            guess = int(input("Yo, guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number, silly!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("Yeah bitch! You got it! My number was {}".format(secret_num))
                break
            # too low message
            elif guess < secret_num:
                print("My number is higher than {}.".format(guess))
            # too high message
            else:
                print("My number is lower than {}.".format(guess))
            guesses.append(guess)
    else:
        print("Sorry not sorry. You didn't get it, kitty girl! My number was {}.".format(secret_num))
    play_again = input("You down to play another round? y/n ")
    if play_again.lower() != "n":
        game()
    else:
        print("Bye!")

game()
