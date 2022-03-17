import random
coins = ['heads', 'tails']
done = False

def coin_toss ():
    user_choice = input("Flipping a coin. Heads or Tails (or Quit)?").lower()
    coin_toss = random.choice(coins)
    print("User choice:", user_choice, "Coin_toss", coin_toss)
    if user_choice == "quit":
        return(True)
    elif user_choice == coin_toss:  #else if
        print("You win!")
    else:
        print("Go home. Loser")
        return(False)

while not done:
    done = coin_toss()

