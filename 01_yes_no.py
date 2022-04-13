# Ask user if they have played before
show_instructions = input("Have you played before?").lower()

# If yes, output 'program continues'
if show_instructions.lower() == "yes":
    print("Program continues")

elif show_instructions == "y":
    print("Program continue")

# If no output 'display instructions'
elif show_instructions.lower() == "no":
    print("Display instructions")

elif show_instructions == "n":
    print("Display instructions")

elif show_instructions.lower() == "maybe":
    print("Please enter yes or no")
