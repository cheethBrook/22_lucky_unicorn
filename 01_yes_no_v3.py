show_instructions = "Have you played before"

while show_instructions.lower() != "Display instructions":
    # Ask user if they have played before
    show_instructions = input("Have you played before?").lower()

    # If yes, output 'program continues'
    if show_instructions.lower() == "yes" or show_instructions == "y":
        print("Program continues")

    # If no output 'display instructions'
    elif show_instructions.lower() == "no" or show_instructions == "n":
        print("Display instructions")

    elif show_instructions.lower() == "maybe":
        print("Please enter yes or no")
