import random

# Main routine goes here


STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 10):
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

    print()
    print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
    print("Final balance: ${:.2f}".format(balance))

    # Output
    print("Token: {} , Balance: ${}".format(chosen_num, balance))
