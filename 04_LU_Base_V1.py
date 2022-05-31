# lucky unicorn base code
import random
# **** Functions go here ****


def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If yes, output 'program continues'
        if response.lower() == "yes" or response == "y":
            response = "yes"
            return response
        # If no output 'display instructions'
        elif response.lower() == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")


def instructions():
    print("*** How to play ***")
    print()
    print("The rules of the game go here")
    print()
    return ""

# number check check value is valid


def num_check(question, low, high):
    error = "Please enter a whole number between 1 & 10\n"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # If the amount is too low / too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)

# **** Main routine ****
# welcome message

# ask user if played before


played_before = yes_no("Have you played the game before? ")
# display instructions if not played before
if played_before == "no" or "n":
    instructions()
    print()

# ask user how much they want to play with 1-10
how_much = num_check("How much would you like to play with? ", 1, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}.   Your balance is "
          "${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit")

print()
print("Final balance", balance)

# print statement for testing
print("You will be spending ${}".format(how_much))
