import random
coins = ['heads', 'tails']
done = False

while not done:
    user_choice = input("Flipping a coin. Heads or Tails (or Quit)?"). lower()
    coin_toss = random.choice(coins)
    print("User choice:", user_choice, "Coin_toss", coin_toss)
    if user_choice == "quit":
        done = True
    elif user_choice == coin_toss:
        print("You win!")
    else:
        print("Go home. Loser")

