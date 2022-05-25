import random

# Main routine goes here
tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 100):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "Unicorn":
        balance += 4
    elif chosen == "Donkey":
        balance -= 1
    else:
        balance -= 0.5

    # output
    print("Token: {}  ,  Balance: ${}".format(chosen, balance))
