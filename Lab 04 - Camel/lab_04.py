user_input=""
iterations = 0

while user_input.lower() != "yes":
    iterations +=1
    if iterations%3 == 0:
        continue
    print("I must not tell lies.", iterations)
    user_input = input("Should I?")

print("Your detention is complete")


