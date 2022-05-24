# Function goes here
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

# Main Routine goes here


show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "yes" or "y":
    print("program continues")
else:
    print("display instructions")
